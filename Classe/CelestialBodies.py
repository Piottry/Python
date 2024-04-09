from ursina.shaders import lit_with_shadows_shader
from ursina import Entity, time, sin, cos
from math import radians

class CelestialBodies(Entity):

    def __init__(self, position=(0,0,0) ,orbitSpeed=(0,0,0) ,rotation =(0,0,0),orbitRadius=0, rotationSpeed=[0,0,0], scale=0, texture=''):
        super().__init__()
        self.model = 'sphere'
        self.collider = 'sphere'
        self.position = position
        self.orbitSpeed = orbitSpeed
        self.rotationSpeed = rotationSpeed
        self.orbitRadius = orbitRadius
        self.scale = scale
        self.shader = lit_with_shadows_shader
        self.texture = texture
        self.rotation= rotation #apply tilt to planet
        
    def update(self):
        self.rotation += [i*time.dt for i in self.rotationSpeed] #self.rotationSpeed*time.dt
        return True
    
    
   
        
