from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
from ursina.shaders import lit_with_shadows_shader
from math import degrees,atan,cos,sin
import openpyxl as op 

from Classe.SolarSystem import SolarSystem
from Classe.Planets import  Planets
from Classe.Sun import Sun

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
        player.y += player.speed * time.dt/10
    if held_keys['control']:
        player.y -= player.speed * time.dt/10
    if held_keys['p']:
        global pause_time 
        pause_time  = not pause_time
        for i in range(0,len(planets)):
            planets[i].pause_time=pause_time

pause_time =True
########################
### Gravity function ###
########################
def force_gravite_p1_p2(p1,p2):
    d=[p1.pos[0]-p2.pos[0],p1.pos[1]-p2.pos[1],p1.pos[2]-p2.pos[2]]     # Distance between the 2 objects in x y & z coordinates
    acc=[0,0,0]

    dist=sqrt(pow(d[0],2)+pow(d[1],2)+pow(d[2],2))      # Straight distance
    
    force=G*p2.mass/pow(dist,2)             # Gravitational interaction force


    ### Calculates and assigns the accelerations, taking into account the position of the 2 objects ###

    if d[0]==0 and d[1]==0 and d[2]==0: # If the 2 objects have the same center, same x y and z coordinates
        acc[0]=-p1.acc[0]
        acc[1]=-p1.acc[1]
        acc[2]=-p1.acc[2]
    
    elif d[0]==0 and d[1]==0:           # If the 2 objects have the same x and y coordinates
        acc[0]=0
        acc[1]==0
        if d[2]>0:
            acc[2]==-force
        else:
            acc[2]==force
    
    elif d[0]==0 and d[2]==0:           # If the 2 objects have the same x and z coordinates
        acc[0]=0
        acc[2]==0
        if d[1]>0:
            acc[1]==-force
        else:
            acc[1]==force

    elif d[1]==0 and d[2]==0:           # If the 2 objects have the same x and z coordinates
        acc[1]=0
        acc[2]==0
        if d[0]>0:
            acc[0]==-force
        else:
            acc[0]==force
    
    elif d[0]==0:                       # If the 2 objects have the same x coordinate
        if d[1]>0:
            acc[1]=-force*cos(atan(sqrt(pow(d[2],2))/d[1]))
        elif d[1]<0:
            acc[1]=force*cos(atan(sqrt(pow(d[2],2))/d[1]))
        
        if d[2]>0:
            acc[2]=-force
        else:
            acc[2]=force
            
    elif d[1]==0:                       # If the 2 objects have the same y coordinate
        if d[0]>0:
            if d[2]>0:
                acc[0]=-force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                acc[2]=-force*cos(atan(abs(d[0])/abs(d[2])))
            else:
                acc[0]=-force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                acc[2]=force*cos(atan(abs(d[0])/abs(d[2])))
        else:
            if d[2]>0:
                acc[0]=force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                acc[2]=-force*cos(atan(abs(d[0])/abs(d[2])))
            else:
                acc[0]=force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                acc[2]=force*cos(atan(abs(d[0])/abs(d[2])))

    elif d[2]==0:                       # If the 2 objects have the same z coordinate
        if d[1]>0:
            acc[1]=-force*cos(atan(sqrt(pow(d[2],2))/d[1]))
        elif d[1]<0:
            acc[1]=force*cos(atan(sqrt(pow(d[2],2))/d[1]))
        
        if d[0]>0:
            acc[0]=-force
        else:
            acc[0]=force
    
    else:                               # If the 2 objects have different coordinate
        if d[1]>0:
            acc[1]=-force*cos(atan(sqrt(pow(d[0],2)+pow(d[2],2))/d[1]))
        elif d[1]<0:
            acc[1]=force*cos(atan(sqrt(pow(d[0],2)+pow(d[2],2))/d[1]))
        
        if d[0]>0:
            if d[2]>0:
                acc[0]=-force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                acc[2]=-force*cos(atan(abs(d[0])/abs(d[2])))
            elif d[2]<0:
                acc[0]=-force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                acc[2]=force*cos(atan(abs(d[0])/abs(d[2])))
        elif d[0]<0:
            if d[2]>0:
                acc[0]=force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                acc[2]=-force*cos(atan(abs(d[0])/abs(d[2])))
            elif d[2]<0:
                acc[0]=force*cos((pi/2) - atan(abs(d[0])/abs(d[2])))
                acc[2]=force*cos(atan(abs(d[0])/abs(d[2])))

    return acc

G=6.67428*pow(10,-11)       # Gravitational constant 


#####################
### Planets & Sun ###
#####################

planets=[]
for i in range(3,11):
    planets.append(Planets(name=sheet['A'+str(i)].value,
                        scale=sheet['B'+str(i)].value,
                        texture=sheet['C'+str(i)].value,

                        position=(sheet['D'+str(i)].value,sheet['E'+str(i)].value,sheet['F'+str(i)].value),
                        vitesse =(sheet['G'+str(i)].value,sheet['H'+str(i)].value,sheet['I'+str(i)].value),

                        obliquity=sheet['J'+str(i)].value,
                        equator=sheet['K'+str(i)].value,
                        rotationSpeed=[sheet['M'+str(i)].value,sheet['N'+str(i)].value,sheet['O'+str(i)].value],     # Mass of the planet

                        mass=sheet['P'+str(i)].value,      # Mass of the planet
                        time=86164.1,#3600,#86164.1,
                        jour=sheet['Q'+str(i)].value
                        )
    )



sun=Sun(name=sheet['A2'].value,
        scale=sheet['B2'].value,
        texture=sheet['C2'].value,

        obliquity=sheet['J'+str(i)].value,
        equator=sheet['K'+str(i)].value,
        rotationSpeed=[sheet['M2'].value,sheet['N2'].value,sheet['O2'].value],     # Mass of the planet

        mass=sheet['P2'].value,      # Mass of the planet
        time=86164.1,#3600,#86164.1,
        jour=sheet['Q2'].value
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
                               position=(100,20,0),
                               gravity=0,
                               speed=50,
                               collider='mesh',
                               )

def update():
    pos_player_6000=0
    if distance(player,sun)<6000:
        dist=distance(player,planets[0])
        for i in range(0,len(planets)):
            if dist>distance(player,planets[i]):
                dist=distance(player,planets[i])       
        player.speed=2.5*dist
    else:
        player.position=pos_player_6000
    
    pos_player_6000=player.position



    global pause_time 
    if pause_time ==False:
        acc=[]

        ###################
        # Sun Interaction #
        ###################
        for i in range(0,len(planets)):
            acc.append(force_gravite_p1_p2(planets[i],sun))

        ########################
        # Planets Interactions #
        ########################
        for i in range(0,len(planets)):
            for y in range(0,len(planets)):
                if y!=i:
                    acc[i]+=force_gravite_p1_p2(planets[i],planets[y])

        ########################
        # Planets Acceleration #
        ########################
        for i in range(0,len(planets)):
            planets[i].acc=acc[i]

camera.clip_plane_far = 20000
    







    


app.run()


