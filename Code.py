from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
from ursina.shaders import lit_with_shadows_shader
from math import degrees
import openpyxl as op 
from Classe.SolarSystem import SolarSystem
from Classe.CelestialBodies import CelestialBodies

data=op.load_workbook("Masses astres.xlsx")
sheet=data["Feuil2"]

app = Ursina()


window.title = 'Game'
window.fps_counter.enabled = True
max_frames = 120
window.fps_counter.max = 120

app.time=0
app.time_dt=0


def input(key):
    global paused
    if held_keys['space']:
        player.y += 100 * time.dt
    if held_keys['control']:
        player.y -= 100 * time.dt




sun=CelestialBodies(position=(sheet['B2'].value,sheet['C2'].value,sheet['D2'].value),orbitSpeed =(sheet['E2'].value, sheet['F2'].value ,sheet['G2'].value),rotation=(sheet['H2'].value,sheet['I2'].value,sheet['J2'].value),orbitRadius=sheet['K2'].value, rotationSpeed=[0,1.99,0],scale=sheet['O2'].value,texture=sheet['P2'].value)
sun.sun=True

mercury=CelestialBodies(position=(sheet['B3'].value,sheet['C3'].value,sheet['D3'].value),orbitSpeed =(sheet['E3'].value, sheet['F3'].value ,sheet['G3'].value),rotation=(sheet['H3'].value,sheet['I3'].value,sheet['J3'].value),orbitRadius=sheet['K3'].value, rotationSpeed=[0,10,89,0],scale=sheet['O3'].value,texture=sheet['P3'].value)
venus=CelestialBodies(position=(sheet['B4'].value,sheet['C4'].value,sheet['D4'].value),orbitSpeed =(sheet['E4'].value, sheet['F4'].value ,sheet['G4'].value),rotation=(sheet['H4'].value,sheet['I4'].value,sheet['J4'].value),orbitRadius=sheet['K4'].value, rotationSpeed=[0,6.52,0],scale=sheet['O4'].value,texture=sheet['P4'].value)
earth=CelestialBodies(position=(sheet['B5'].value,sheet['C5'].value,sheet['D5'].value),orbitSpeed =(sheet['E5'].value, sheet['F5'].value ,sheet['G5'].value),rotation=(sheet['H5'].value,sheet['I5'].value,sheet['J5'].value),orbitRadius=sheet['K5'].value, rotationSpeed=[0,17000,0],scale=sheet['O5'].value,texture=sheet['P5'].value)
mars=CelestialBodies(position=(sheet['B6'].value,sheet['C6'].value,sheet['D6'].value),orbitSpeed =(sheet['E6'].value, sheet['F6'].value ,sheet['G6'].value),rotation=(sheet['H6'].value,sheet['I6'].value,sheet['J6'].value),orbitRadius=sheet['K6'].value, rotationSpeed=[0,-360/24,0],scale=sheet['O6'].value,texture=sheet['P6'].value)
jupiter=CelestialBodies(position=(sheet['B7'].value,sheet['C7'].value,sheet['D7'].value),orbitSpeed =(sheet['E7'].value, sheet['F7'].value ,sheet['G7'].value),rotation=(sheet['H7'].value,sheet['I7'].value,sheet['J7'].value),orbitRadius=sheet['K7'].value, rotationSpeed=[0,-360/24,0],scale=sheet['O7'].value,texture=sheet['P7'].value)
saturn=CelestialBodies(position=(sheet['B8'].value,sheet['C8'].value,sheet['D8'].value),orbitSpeed =(sheet['E8'].value, sheet['F8'].value ,sheet['G8'].value),rotation=(sheet['H8'].value,sheet['I8'].value,sheet['J8'].value),orbitRadius=sheet['K8'].value, rotationSpeed=[0,-360/24,0],scale=sheet['O8'].value,texture=sheet['P8'].value)
uranus=CelestialBodies(position=(sheet['B9'].value,sheet['C9'].value,sheet['D9'].value),orbitSpeed =(sheet['E9'].value, sheet['F9'].value ,sheet['G9'].value),rotation=(sheet['H9'].value,sheet['I9'].value,sheet['J9'].value),orbitRadius=sheet['K9'].value, rotationSpeed=[0,-360/24,0],scale=sheet['O9'].value,texture=sheet['P9'].value)
neptune=CelestialBodies(position=(sheet['B10'].value,sheet['C10'].value,sheet['D10'].value),orbitSpeed =(sheet['E10'].value, sheet['F10'].value ,sheet['G10'].value),rotation=(sheet['H10'].value,sheet['I10'].value,sheet['J10'].value),orbitRadius=sheet['K10'].value, rotationSpeed=[0,-360/24,0],scale=sheet['O10'].value,texture=sheet['P10'].value)



### MOONS ###
#moon = CelestialBodies(80,2,0,0.05,'assets/Moon')



### TRUC ###
#saturnRing=Entity(model="assets/saturnring.obj",
                #scale=1,
                #parent=saturn,
                #texture='assets/saturn_ring',
                #position=(0, 0, 0),
                #rotation=(0,0,23),
                #)




sky=Sky(texture="assets/space")
EditorCamera()

player = FirstPersonController(model="sphere",
                               color='white',
                               height=0,
                               position=(100, 0, 1),
                               gravity=0,
                               speed=5,
                               collider='sphere',
                               )



app.run()


