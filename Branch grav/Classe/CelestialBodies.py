from ursina.shaders import lit_with_shadows_shader
from ursina import Entity, time, sin, cos, Vec3
from math import *


class CelestialBodies(Entity):

    def __init__(self , name , position=(0,0,0) ,orbitSpeed=(0.0,0.0,0.0) ,rotation =(0,0,0), rotationSpeed=[0,0,0], scale=0, texture='',mass=0):
        super().__init__()
        self.name=name
        self.model = 'sphere'#'/assets/mesh/planet.obj'#
        self.collider = 'mesh'
        self.scale = scale
        self.texture = texture


        self.pos=Vec3(position)
        self.vit=Vec3(orbitSpeed)
        self.acc=Vec3((-100000000,0,0))
        self.mass=mass
        
        self.position = [x *pow(10,-9)  for x in self.pos]

        self.rotation= rotation #apply tilt to planet
        self.rotationSpeed = rotationSpeed
        
    def update(self):
        self.rotation += [i*time.dt for i in self.rotationSpeed] #0.1 s instead of time.dt ###to modify

        self.vit+=[x *0.1 for x in self.acc]
        self.pos+=[x *0.1  for x in self.vit]

        self.position=[x *pow(10,-9)  for x in self.pos] #(self.pos[0]*pow(10,-9),self.pos[1]*pow(10,-9),self.pos[2]*pow(10,-9))

        for i in range(0,2):
             if self.acc[i]!=0:
                if self.position[i]>0:
                    self.acc[i]=-abs(self.acc[i])
                if self.position[i]<0:
                    self.acc[i]=abs(self.acc[i])
                  


        return True
    
    
   
        
