from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
from math import degrees,atan,cos,sin

import openpyxl as op 

from Classe.Planets import  Planets
from Classe.Sun import Sun
from Classe.Moon import Moon
from Classe.Clouds import Clouds

### Load and keep in a variable the Excel file
data=op.load_workbook("Masses astres.xlsx")
sheet=data["Feuil2"]


###Create our app
app = Ursina()




window.title = 'Game'
window.fps_counter.enabled = False
window.fullscreen=True

app.time=0
app.time_dt=0

### A bunch of possible simulation time
simu_possible_time=[1,6300,86164.1,86164.1*365.25]
simu_time=86164.1
simu_time_counter=2

#####################
### Key detection ###
#####################
def input(key):
    global simu_time_counter
    global simu_time

    ### UP and Down
    if held_keys['space']:
        player.y += player.speed * time.dt
    if held_keys['control']:
        player.y -= player.speed * time.dt

    ### Pause key
    if key == 'p':
        global pause_time 
        pause_time  = not pause_time
        for i in range(0,len(planets)):
            planets[i].pause_time=pause_time
        for i in range(0,len(clouds)):
            clouds[i].pause_time=pause_time
        
        sun.pause_time=pause_time
        for i in range(0,len(moons)):
            moons[i].pause_time=pause_time
    
    ### Allow the player to teleport to a planet
    if key == '1':
        player.position=planets[0].position
    if key == '2':
        player.position=planets[1].position
    if key == '3':
        player.position=planets[2].position
    if key == '4':
        player.position=planets[3].position
    if key == '5':
        player.position=planets[4].position
    if key == '6':
        player.position=planets[5].position
    if key == '7':
        player.position=planets[6].position
    if key == '8':
        player.position=planets[7].position
    
    if key == 'escape':
        quit()
    
    ### Unlock player
    if key == 'u':          
        player.position=(player.position[0],player.position[1]+20,player.position[2])

    ### Change the time step
    if key == 'up arrow' or key == 'down arrow':
        if key == 'up arrow' and simu_time_counter<3:
            simu_time_counter+=1
            simu_time=simu_possible_time[simu_time_counter]
        if key == 'down arrow' and simu_time_counter>0:
            simu_time_counter-=1
            simu_time=simu_possible_time[simu_time_counter]
        
        for i in range(0,len(planets)):
            planets[i].time=simu_time
        sun.time=simu_time
        for i in range(0,len(moons)):
            moons[i].time=simu_time
        

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



###########
### Sun ###
###########

i=2
sun=Sun(name=sheet['A'+str(i)].value,       # Name of the entity
        scale=sheet['B'+str(i)].value,
        texture=sheet['C'+str(i)].value,

        position=(sheet['D'+str(i)].value,sheet['E'+str(i)].value,sheet['F'+str(i)].value),     # Position in X Y Z 
        vitesse =(sheet['G'+str(i)].value,sheet['H'+str(i)].value,sheet['I'+str(i)].value),     # Speed in X Y Z 

        obliquity=sheet['J'+str(i)].value,
        equator=sheet['K'+str(i)].value,

        rotationSpeed=[sheet['M'+str(i)].value,sheet['N'+str(i)].value,sheet['O'+str(i)].value],     # Specifie the axes of rotation

        mass=sheet['P'+str(i)].value,       # Mass of the planet
        time=simu_time,#3600,#86164.1,      
        jour=sheet['Q'+str(i)].value        # A full rotation around Y axe
)


###############
### Planets ###
###############

planets=[]
i+=1
while sheet['A'+str(i)].value:      # Declares planet until there are a blank on the Excel file
    planets.append(Planets(name=sheet['A'+str(i)].value,
                        scale=sheet['B'+str(i)].value,
                        texture=sheet['C'+str(i)].value,

                        position=(sheet['D'+str(i)].value,sheet['E'+str(i)].value,sheet['F'+str(i)].value),
                        vitesse =(sheet['G'+str(i)].value,sheet['H'+str(i)].value,sheet['I'+str(i)].value),

                        obliquity=sheet['J'+str(i)].value,
                        equator=sheet['K'+str(i)].value,
                        rotationSpeed=[sheet['M'+str(i)].value,sheet['N'+str(i)].value,sheet['O'+str(i)].value],     # Mass of the planet

                        mass=sheet['P'+str(i)].value,      # Mass of the planet
                        time=simu_time,#3600,#86164.1,
                        jour=sheet['Q'+str(i)].value
                        )
    )
    i+=1
i+=1


#############
### Moons ###
#############

moons=[]
i=12
while sheet['A'+str(i)].value:
    moons.append(Moon(name=sheet['A'+str(i)].value,
                    scale=sheet['B'+str(i)].value,
                    texture=sheet['C'+str(i)].value,
            
                    position=(sheet['D'+str(i)].value + sheet['D'+str(sheet['R'+str(i)].value)].value  ,  sheet['E'+str(i)].value + sheet['E'+str(sheet['R'+str(i)].value)].value  ,  sheet['F'+str(i)].value),#+planets[sheet['R'+str(i)].value].position[2]
                    vitesse =(sheet['G'+str(i)].value,sheet['H'+str(i)].value,sheet['I'+str(i)].value+sheet['I'+str(sheet['R'+str(i)].value)].value),#+sheet['I'+str(sheet['R'+str(i)].value)].value

                    obliquity=sheet['J'+str(i)].value,
                    equator=sheet['K'+str(i)].value,
                    rotationSpeed=[sheet['M'+str(i)].value,sheet['N'+str(i)].value,sheet['O'+str(i)].value],     # Mass of the planet

                    mass=sheet['P'+str(i)].value,      # Mass of the planet
                    time=simu_time,
                    jour=sheet['Q'+str(i)].value,

                    planet_number=sheet['R'+str(i)].value-3     # Store the coresponding planet
                    )
    )
    i+=1



#############
### Other ###
#############

# Earth clouds
clouds=[]
for i in range(1,4):
    clouds.append(Clouds(planets=planets[2],    # Earth
                         texture_num=i,
                         alpha=0.05         # Transparency
                         )
                 )

### Saturn ring
ring=Entity(model=load_model('assets/mesh/torus.obj'),
            texture='assets/textures/saturn_ring',
            position=planets[5].position,
            scale=(3.5,0.1,3.5),
            rotation=planets[5].rotation,
            alpha=0.8
)




### Space
sky=Sky(texture="assets/textures/space")

EditorCamera()

### Our player
player = FirstPersonController(model="assets/mesh/planet.obj",
                               color='white',
                               texture='space.png',
                               alpha=0.2,
                               height=0,
                               position=(100,10,0),
                               gravity=0,
                               speed=50
                               )




### Update every time.dt
def update():
    ### Player speed and map limit ###
    pos_player_lim=0
    if distance(player,sun)<10000:
        dist=distance(player,planets[0])
        for i in range(0,len(planets)):
            if dist>distance(player,planets[i]):
                dist=distance(player,planets[i])       
        player.speed=2.5*dist
    else:
        player.position=pos_player_lim
    
    pos_player_lim=player.position

    



    
    
    planet_acc=[]

    ###################
    # Sun Interaction #
    ###################
    for i in range(0,len(planets)):
        planet_acc.append(force_gravite_p1_p2(planets[i],sun))

    ########################
    # Planets Interactions #
    ########################
    for i in range(0,len(planets)):
        for y in range(0,len(planets)):
            if y!=i:
                planet_acc[i]+=force_gravite_p1_p2(planets[i],planets[y])
        
    ########################
    # Planets Acceleration #
    ########################
    for i in range(0,len(planets)):
        planets[i].acc=planet_acc[i]


        
    ######################
    # Moons Interactions #
    ######################

    '''
    moon_acc=0
    #moon_acc=force_gravite_p1_p2(moons[0],planets[moons[0].planet_number])
    moon_acc=force_gravite_p1_p2(moons[0],sun)
    #force_gravite_p1_p2(moons[0],sun)
    moons[0].acc=moon_acc
    '''

    #####################
    # Ring displacement #
    #####################
    ring.position=planets[5].position
    ring.rotate([x*360*time.dt*planets[5].time/planets[5].jour_propre for x in planets[5].rotationSpeed])


camera.clip_plane_far = 20000       # Allow greatter render distance

# Run the app
app.run()


