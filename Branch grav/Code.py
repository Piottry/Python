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

def force_gravite_p1_p2(p1,p2):
    d=(p1.pos[0]-p2.position[0],p1.pos[1]-p2.position[1],p1.pos[2]-p2.position[2])
    dist=sqrt(pow(d[0],2)+pow(d[1],2)+pow(d[2],2))
    force=-G*p2.mass/dist
    '''
    if d[0]>0 & d[0]>0 & d[0]>0:
        p1.acc[0]=-G*p2.mass/dist
        p1.acc[1]=-G*p2.mass/dist
        p1.acc[2]=-G*p2.mass/dist
    elif d[0]>0 & d[0]>0 & d[0]<0:
        p1.acc[0]=-G*p2.mass/dist
        p1.acc[1]=-G*p2.mass/dist
        p1.acc[2]=G*p2.mass/dist
    elif d[0]<0 & d[0]>0 & d[0]<0:
        p1.acc[0]=G*p2.mass/dist
        p1.acc[1]=-G*p2.mass/dist
        p1.acc[2]=G*p2.mass/dist
    elif d[0]<0 & d[0]>0 & d[0]>0:
        p1.acc[0]=G*p2.mass/dist
        p1.acc[1]=-G*p2.mass/dist
        p1.acc[2]=-G*p2.mass/dist
    elif d[0]>0 & d[0]<0 & d[0]>0:
        p1.acc[0]=-G*p2.mass/dist
        p1.acc[1]=G*p2.mass/dist
        p1.acc[2]=-G*p2.mass/dist
    elif d[0]>0 & d[0]<0 & d[0]<0:
        p1.acc[0]=-G*p2.mass/dist
        p1.acc[1]=G*p2.mass/dist
        p1.acc[2]=G*p2.mass/dist
    elif d[0]<0 & d[0]<0 & d[0]<0:
        p1.acc[0]=G*p2.mass/dist
        p1.acc[1]=G*p2.mass/dist
        p1.acc[2]=G*p2.mass/dist
    elif d[0]<0 & d[0]<0 & d[0]>0:
        p1.acc[0]=G*p2.mass/dist
        p1.acc[1]=G*p2.mass/dist
        p1.acc[2]=-G*p2.mass/dist
    '''
    return force

G=6.67428*pow(10,-11)


#####################
### Planets & Sun ###
#####################

planets_sun=[]
i=5

#####################
###  Real values  ###
#####################
planets=CelestialBodies(name=sheet['A'+str(i)].value,
                            scale=sheet['O'+str(i)].value,
                            texture=sheet['P'+str(i)].value,
                                       
                            #position=(sheet['B'+str(i)].value,sheet['C'+str(i)].value,sheet['D'+str(i)].value),
                            position=(149597887500,0,0),
                            orbitSpeed =(1000000000,0,0),
                                       
                                       
                            rotation=(sheet['H'+str(i)].value,sheet['I'+str(i)].value,sheet['J'+str(i)].value),
                            rotationSpeed=[sheet['L'+str(i)].value, sheet['M'+str(i)].value ,sheet['N'+str(i)].value],
                            #orbitRadius=sheet['K'+str(i)].value, 
                                       
                                       
                            mass=0
                            )
                                       




soleil=Entity(model = 'sphere',
              collider = 'mesh',
                position=(0,0,0),
                texture='assets/textures/8k_sun',
                scale=100,
                mass=1.988*pow(10,30)
)




#############
### Moons ###
#############
'''
i+=1
while sheet['A'+str(i)].value:
    planets_sun.append(CelestialBodies(name=sheet['A'+str(i)].value,
                                       position=(sheet['B'+str(i)].value,sheet['C'+str(i)].value,sheet['D'+str(i)].value),
                                       orbitSpeed =(sheet['E'+str(i)].value, sheet['F'+str(i)].value ,sheet['G'+str(i)].value),
                                       rotation=(sheet['H'+str(i)].value,sheet['I'+str(i)].value,sheet['J'+str(i)].value),
                                       orbitRadius=sheet['K'+str(i)].value, 
                                       rotationSpeed=[sheet['L'+str(i)].value, sheet['M'+str(i)].value ,sheet['N'+str(i)].value],
                                       scale=sheet['O'+str(i)].value,
                                       texture=sheet['P'+str(i)].value,
                                       mass=0,
                                       alpha=0
                                       )
                                       )
    i+=1
i+=1
'''

#############
### Other ###
#############








sky=Sky(texture="assets/textures/space")
EditorCamera()

player = FirstPersonController(model="assets/mesh/planet.obj",
                               color='white',
                               alpha=0.2,
                               height=0,
                               position=(100, 0, 0),
                               gravity=0,
                               speed=50,
                               collider='mesh',
                               )

def update():

    force=force_gravite_p1_p2(planets,soleil)
    #print(force)
    #planets.acc[0]=force
    print(force)


    


app.run()


