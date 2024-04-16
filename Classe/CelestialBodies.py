from ursina.shaders import lit_with_shadows_shader
from ursina import Entity, time, sin, cos, Vec3
from math import radians

class CelestialBodies(Entity):

    def __init__(self , name , position=(0,0,0) ,orbitSpeed=(0,0,0) ,rotation =(0,0,0),orbitRadius=0, rotationSpeed=[0,0,0], scale=0, texture=''):
        super().__init__()
        self.name=name
        self.model = '/assets/mesh/planet.obj'#'sphere'#
        self.collider = 'mesh'
        self.position = position
        self.orbitSpeed = orbitSpeed

        self.orbitRadius = orbitRadius
        self.scale = scale

        #self.texture = texture

        self.rotation= rotation #apply tilt to planet
        self.rotationSpeed = rotationSpeed
        
    def update(self):
        self.rotation += [i*time.dt for i in self.rotationSpeed] #self.rotationSpeed*time.dt
        return True
    
    
   
        
