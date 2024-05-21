from ursina import Entity, time, sin, cos, Vec3
from math import *


class Planets(Entity):
    def __init__(self , name, scale=1 , texture='',position=(0,0,0),vitesse=(0,0,0),equator=0,obliquity=0, rotationSpeed=[0,0,0],mass=0,time=1,jour=1,pause=True):
        super().__init__()
        self.name=name              # Name of the Planet
        self.model = 'sphere'       # The model is a shpere
        self.scale = scale          # Size of the model scale with a factor witch is not the same as the distance
        self.texture = texture      # Texture applied on the model

        self.pause_time=pause       # Pause enable or disable

        self.time=time              # Simulation time
        self.jour_propre=jour       # Full rotation around Y axe

        self.pos=Vec3(position)     # Real position
        self.vit=Vec3(vitesse)      # Real speed
        self.acc=Vec3((0,0,0))      # Real acceleration
        
        self.mass=mass              # Mass of the planet
        
        self.position = [x *2*pow(10,-9)  for x in self.pos]        # Fake position downscaled with a 0,000000002 factor for distances

        self.rotation=(obliquity,0,0)   # Rotation of the planet on X Y Z


        self.rotationSpeed = rotationSpeed  # Rotation direction



    ### Update every time.dt
    def update(self):
        
        
        ### If not paused
        if self.pause_time==False:

            self.rotate([x*360*time.dt*self.time/self.jour_propre for x in self.rotationSpeed])     # Rotate with consideration of time

            ### Calculate speed and acceleration
            self.vit+=[x * time.dt*self.time for x in self.acc]
            self.pos+=[x * time.dt*self.time  for x in self.vit]

            self.position=[x *2*pow(10,-9)  for x in self.pos]      # Downscale to display planet



        return True

    
   
        
