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
window.fps_counter.enabled = False
window.fullscreen=True

app.time=0
app.time_dt=0

#####################
### Key detection ###
#####################
def input(key):
    global paused
    if held_keys['space']:
        player.y += 100 * time.dt
    if held_keys['control']:
        player.y -= 100 * time.dt

#####################
### Planets & Sun ###
#####################

planets_sun=[]
i=2
while sheet['A'+str(i)].value:
    planets_sun.append(CelestialBodies(name=sheet['A'+str(i)].value,
                                       position=(sheet['B'+str(i)].value,sheet['C'+str(i)].value,sheet['D'+str(i)].value),
                                       orbitSpeed =(sheet['E'+str(i)].value, sheet['F'+str(i)].value ,sheet['G'+str(i)].value),
                                       rotation=(sheet['H'+str(i)].value,sheet['I'+str(i)].value,sheet['J'+str(i)].value),
                                       orbitRadius=sheet['K'+str(i)].value, 
                                       rotationSpeed=[sheet['L'+str(i)].value, sheet['M'+str(i)].value ,sheet['N'+str(i)].value],
                                       scale=sheet['O'+str(i)].value,
                                       texture=sheet['P'+str(i)].value,
                                       mass=0
                                       )
                                       )
    i+=1
i+=1
planets_sun[0].sun=True




#############
### Moons ###
#############
moons=[]
while sheet['A'+str(i)].value:
    moons.append(CelestialBodies(name=sheet['A'+str(i)].value,
                                 position=(sheet['B'+str(i)].value,sheet['C'+str(i)].value,sheet['D'+str(i)].value),
                                 orbitSpeed =(sheet['E'+str(i)].value, sheet['F'+str(i)].value ,sheet['G'+str(i)].value),
                                 rotation=(sheet['H'+str(i)].value,sheet['I'+str(i)].value,sheet['J'+str(i)].value),
                                 orbitRadius=sheet['K'+str(i)].value, 
                                 rotationSpeed=[sheet['L'+str(i)].value, sheet['M'+str(i)].value ,sheet['N'+str(i)].value],
                                 scale=sheet['O'+str(i)].value,
                                 texture=sheet['P'+str(i)].value
                                 )
                                 )
    i+=1
i+=1

#############
### Other ###
#############
other=[]
while sheet['A'+str(i)].value:
    other.append(CelestialBodies(name=sheet['A'+str(i)].value,
                                 position=(sheet['B'+str(i)].value,sheet['C'+str(i)].value,sheet['D'+str(i)].value),
                                       orbitSpeed =(sheet['E'+str(i)].value, sheet['F'+str(i)].value ,sheet['G'+str(i)].value),
                                       rotation=(sheet['H'+str(i)].value,sheet['I'+str(i)].value,sheet['J'+str(i)].value),
                                       orbitRadius=sheet['K'+str(i)].value, 
                                       rotationSpeed=[sheet['L'+str(i)].value, sheet['M'+str(i)].value ,sheet['N'+str(i)].value],
                                       scale=sheet['O'+str(i)].value,
                                       texture=sheet['P'+str(i)].value
                                       )
                                       )
    i+=1








sky=Sky(texture="assets/textures/space")
EditorCamera()

player = FirstPersonController(model="assets/mesh/planet.obj",
                               texture='assets/textures/uranus',
                               height=0,
                               position=(100, 0, 1),
                               gravity=0,
                               speed=50,
                               collider='mesh',
                               )


#PointLight(y=0,color="white10")

app.run()


