from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
from ursina.shaders import lit_with_shadows_shader
from math import degrees,atan,cos,sin
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

########################
### Gravity function ###
########################
def force_gravite_p1_p2(p1,p2):
    d=[p1.pos[0]-p2.pos[0],p1.pos[1]-p2.pos[1],p1.pos[2]-p2.pos[2]]     # Distance between the 2 objects in x y & z coordinates


    dist=sqrt(pow(d[0],2)+pow(d[1],2)+pow(d[2],2))      # Straight distance
    
    force=G*p2.mass/pow(dist,2)             # Gravitational interaction force


    ### Calculates and assigns the accelerations, taking into account the position of the 2 objects ###

    if d[0]==0 and d[1]==0 and d[2]==0: # If the 2 objects have the same center, same x y and z coordinates
        p1.acc[0]=-p1.acc[0]
        p1.acc[1]=-p1.acc[1]
        p1.acc[2]=-p1.acc[2]
    
    elif d[0]==0 and d[1]==0:           # If the 2 objects have the same x and y coordinates
        p1.acc[0]=0
        p1.acc[1]==0
        if d[2]>0:
            p1.acc[2]==-force
        else:
            p1.acc[2]==force
    
    elif d[0]==0 and d[2]==0:           # If the 2 objects have the same x and z coordinates
        p1.acc[0]=0
        p1.acc[2]==0
        if d[1]>0:
            p1.acc[1]==-force
        else:
            p1.acc[1]==force

    elif d[1]==0 and d[2]==0:           # If the 2 objects have the same x and z coordinates
        p1.acc[1]=0
        p1.acc[2]==0
        if d[0]>0:
            p1.acc[0]==-force
        else:
            p1.acc[0]==force
    
    elif d[0]==0:                       # If the 2 objects have the same x coordinate
        if d[1]>0:
            p1.acc[1]=-force*cos(atan(sqrt(pow(d[2],2))/d[1]))
        elif d[1]<0:
            p1.acc[1]=force*cos(atan(sqrt(pow(d[2],2))/d[1]))
        
        if d[2]>0:
            p1.acc[2]=-force
        else:
            p1.acc[2]=force
            
    elif d[1]==0:                       # If the 2 objects have the same y coordinate
        if d[0]>0:
            if d[2]>0:
                p1.acc[0]=-force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                p1.acc[2]=-force*cos(atan(abs(d[0])/abs(d[2])))
            else:
                p1.acc[0]=-force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                p1.acc[2]=force*cos(atan(abs(d[0])/abs(d[2])))
        else:
            if d[2]>0:
                p1.acc[0]=force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                p1.acc[2]=-force*cos(atan(abs(d[0])/abs(d[2])))
            else:
                p1.acc[0]=force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                p1.acc[2]=force*cos(atan(abs(d[0])/abs(d[2])))

    elif d[2]==0:                       # If the 2 objects have the same z coordinate
        if d[1]>0:
            p1.acc[1]=-force*cos(atan(sqrt(pow(d[2],2))/d[1]))
        elif d[1]<0:
            p1.acc[1]=force*cos(atan(sqrt(pow(d[2],2))/d[1]))
        
        if d[0]>0:
            p1.acc[0]=-force
        else:
            p1.acc[0]=force
    
    else:                               # If the 2 objects have different coordinate
        if d[1]>0:
            p1.acc[1]=-force*cos(atan(sqrt(pow(d[0],2)+pow(d[2],2))/d[1]))
        elif d[1]<0:
            p1.acc[1]=force*cos(atan(sqrt(pow(d[0],2)+pow(d[2],2))/d[1]))
        
        if d[0]>0:
            if d[2]>0:
                p1.acc[0]=-force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                p1.acc[2]=-force*cos(atan(abs(d[0])/abs(d[2])))
            elif d[2]<0:
                p1.acc[0]=-force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                p1.acc[2]=force*cos(atan(abs(d[0])/abs(d[2])))
        elif d[0]<0:
            if d[2]>0:
                p1.acc[0]=force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                p1.acc[2]=-force*cos(atan(abs(d[0])/abs(d[2])))
            elif d[2]<0:
                p1.acc[0]=force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                p1.acc[2]=force*cos(atan(abs(d[0])/abs(d[2])))

    return True

G=6.67428*pow(10,-11)       # Gravitational constant 


#####################
### Planets & Sun ###
#####################

planets=[]
for i in range(3,6):
    planets.append(CelestialBodies(name=sheet['A'+str(i)].value,
                        scale=sheet['B'+str(i)].value,
                        texture=sheet['C'+str(i)].value,

                        position=(sheet['D'+str(i)].value,sheet['E'+str(i)].value,sheet['F'+str(i)].value),
                        vitesse =(sheet['G'+str(i)].value,sheet['H'+str(i)].value,sheet['I'+str(i)].value),

                        rotation=(sheet['J'+str(i)].value,sheet['K'+str(i)].value,sheet['L'+str(i)].value),
                        rotationSpeed=[sheet['M'+str(i)].value,sheet['N'+str(i)].value,sheet['O'+str(i)].value],     # Mass of the planet

                        mass=sheet['P'+str(i)].value,      # Mass of the planet
                        time=100,     # One day = time second (10 s)
                        jour=sheet['Q'+str(i)].value
                        )
    )


i=8
'''
planets_saturn=CelestialBodies(name=sheet['A'+str(i)].value,
                        scale=sheet['B'+str(i)].value,
                        texture=sheet['C'+str(i)].value,

                        position=(sheet['D'+str(i)].value,sheet['E'+str(i)].value,sheet['F'+str(i)].value),
                        vitesse =(sheet['G'+str(i)].value,sheet['H'+str(i)].value,sheet['I'+str(i)].value),

                        rotation=(sheet['J'+str(i)].value,sheet['K'+str(i)].value,sheet['L'+str(i)].value),
                        rotationSpeed=[sheet['M'+str(i)].value,sheet['N'+str(i)].value,sheet['O'+str(i)].value],     # Mass of the planet

                        mass=sheet['P'+str(i)].value,      # Mass of the planet
                        time=0.1,     # One day = time second (10 s)
                        jour=sheet['Q'+str(i)].value
                        )
'''



soleil=Entity(model = '/assets/mesh/planet.obj',
                position=(0,0,0),
                pos=(0,0,0),
                texture='assets/textures/8k_sun',
                scale=50,
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
                               texture='space.png',
                               alpha=0.2,
                               height=0,
                               position=(planets[0].pos[0]*pow(10,-9), planets[0].pos[1]*pow(10,-9), planets[0].pos[2]*pow(10,-9)),
                               gravity=0,
                               speed=50,
                               collider='mesh',
                               )

def update():


    ###################
    # Sun Interaction #
    ###################
    for i in range(0,len(planets)):
        force_gravite_p1_p2(planets[i],soleil)







    


app.run()


