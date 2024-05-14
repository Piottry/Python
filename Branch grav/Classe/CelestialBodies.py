from ursina.shaders import lit_with_shadows_shader
from ursina import Entity, time, sin, cos, Vec3
from math import *


class CelestialBodies(Entity):

    def __init__(self , name, scale=1 , texture='', position=(0,0,0) ,vitesse=(0,0,0) ,rotation =(0,0,0), rotationSpeed=[0,0,0],mass=0,time=1,jour=1):
        super().__init__()
        self.name=name
        self.model = 'sphere'#'/assets/mesh/planet.obj'#
        self.collider = 'mesh'
        self.scale = scale
        self.texture = texture

        self.time=time
        self.jour=jour

        self.pos=Vec3(position)
        self.vit=Vec3(vitesse)
        self.acc=Vec3((0,0,0))
        
        self.mass=mass
        
        self.position = [x *pow(10,-9)  for x in self.pos]

        self.rotation= rotation #apply tilt to planet
        self.rotationSpeed = rotationSpeed
        
    def update(self):
        
        self.rotation[1] +=360*0.01
        self.vit+=[x * time.dt*86164.1 for x in self.acc]
        self.pos+=[x * time.dt*86164.1  for x in self.vit]

        self.position=[x *pow(10,-9)  for x in self.pos]



        return True

    
   
        
