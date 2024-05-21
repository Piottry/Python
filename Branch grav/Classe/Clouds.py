from ursina import *
from random import randint

class Clouds(Entity):
    def __init__(self , planets, texture_num, alpha , pause_time=True):
        super().__init__()
        self.model='sphere'
        self.collider='mesh'
        self.scale=planets.scale+planets.scale*randint(8,24)/1000
        self.texture='assets/textures/clouds_'+str(texture_num)
        self.position=planets.position
        self.rotation_x=planets.rotation_x
        self.alpha=alpha
        self.planets=planets
        self.pause_time=pause_time





        
    def update(self):
        if self.pause_time==False:      # If time not paused
            self.position=self.planets.position     # Follow planet position
            self.rotate([x *360*time.dt*self.planets.time/(self.planets.jour_propre+randint(0,10000)-5000) for x in self.planets.rotationSpeed])    # Rotate a bit faster or slower than the planet
        return True
