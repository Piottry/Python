from ursina.shaders import lit_with_shadows_shader
from ursina import Entity, time, sin, cos, Vec3
from math import *


class Planets(Entity):

    def __init__(self , name, scale=1 , texture='',position=(0,0,0),vitesse=(0,0,0),equator=0,obliquity=0, rotationSpeed=[0,0,0],mass=0,time=1,jour=1,pause=True):
        super().__init__()
        self.name=name
        self.model = 'sphere'#'/assets/mesh/planet.obj'#
        self.collider = 'mesh'
        self.scale = scale
        self.texture = texture

        self.pause_time=pause

        self.time=time
        self.jour_propre=jour

        self.pos=Vec3(position)
        self.vit=Vec3(vitesse)
        self.acc=Vec3((0,0,0))
        
        self.mass=mass
        
        self.position = [x *pow(10,-9)  for x in self.pos]

        self.rotation= (equator,0,0)
        self.rotationSpeed = rotationSpeed

        self.rotation_directions

        
    def update(self):
        
        

        if self.pause_time==False:
            
            self.rotation +=[x *360*time.dt*self.time/self.jour_propre for x in self.rotationSpeed]
            
            self.vit+=[x * time.dt*self.time for x in self.acc]
            self.pos+=[x * time.dt*self.time  for x in self.vit]

            self.position=[x *pow(10,-9)  for x in self.pos]



        return True

    
   
        
