from ursina.shaders import lit_with_shadows_shader
from ursina import Entity, time, sin, cos, Vec3
from math import *


class Sun(Entity):

    def __init__(self , name, scale=1 , texture='',obliquity =0,equator=0, rotationSpeed=[0,0,0],mass=0,time=1,jour=1,pause=True):
        super().__init__()
        self.name=name
        self.model = 'sphere'#'/assets/mesh/planet.obj'#
        self.collider = 'mesh'
        self.scale = scale
        self.texture = texture

        self.pause_time=pause

        self.time=time
        self.jour_propre=jour
        
        self.mass=mass
        
        self.position = (0,0,0)
        self.pos=(0,0,0)

        self.rotation= (equator,0,0) #apply tilt to planet
        self.rotationSpeed = rotationSpeed
        
    def update(self):
        
        if self.pause_time==False:
            self.rotation +=[x *360*time.dt*self.time/self.jour_propre for x in self.rotationSpeed]



        return True

    
   
        
