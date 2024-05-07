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
        self.acc=Vec3((0,0,0))
        self.mass=mass
        
        self.position = (position[0]*pow(10,-6),0,0)

        self.rotation= rotation #apply tilt to planet
        self.rotationSpeed = rotationSpeed
        
    def update(self):
        self.rotation += [i*time.dt for i in self.rotationSpeed] #self.rotationSpeed*time.dt
        self.acc=Vec3((-10000,0,0))
        self.vit+=[x * 1 for x in self.acc]
        self.pos+=[x * 1 for x in self.vit]

        self.position=(self.pos[0]*pow(10,-6),0,0)


        if self.acc[0]!=0:
                if self.position[0]>0:
                    self.acc[0]=-abs(self.acc[0])
                if self.position[0]<0:
                    self.acc[0]=abs(self.acc[0])

        return True
    
    
   
        
