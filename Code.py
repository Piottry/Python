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




sun = CelestialBodies(position=(0,0,0),scale=50,texture='assets/8k_sun')
sun.sun=True

#mercury=CelestialBodies(position=(60,0,0), scale=0.35035,texture='assets/mercury')
#venus=CelestialBodies(70,0,0,0.8609,'assets/venus1')
earth=CelestialBodies(position=(sheet['B5'].value,sheet['C5'].value,sheet['D5'].value),orbitSpeed =(360/365, 0 ,0),rotation=(23.45,0,0),orbitRadius=80, rotationSpeed=[0,-360/24,0],scale=0.9159,texture='assets/earth')
#earth=CelestialBodies(position=(80,0,0),orbitSpeed =(360/365, 0 ,0),rotation=(23.45,0,0),orbitRadius=80, rotationSpeed=[0,-360/24,0],scale=0.9159,texture='assets/earth')

#mars=CelestialBodies(90,0,0,0.4876,'assets/mars')
#jupiter=CelestialBodies(110,0,0,10.2667,'assets/jupiter')
#saturn=CelestialBodies(140,0,0,3.5562,'assets/saturn')
#uranus=CelestialBodies(180,0,0,3.6704,'assets/uranus')
#neptune = CelestialBodies(210,0,0,3.5562,'assets/neptune')



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


