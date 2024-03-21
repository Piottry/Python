from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint
from ursina.shaders import lit_with_shadows_shader
from math import degrees


app = Ursina()

window.title = 'Game'
window.fps_counter.enabled = True
max_frames = 120
window.fps_counter.max = 120

app.time=0
app.time_dt=0

def update():

    app.time+=time.dt

    '''
    
    '''

    
    if app.time-app.time_dt > 0.1:
        app.time_dt==app.time

        sun.rotation_y+=0.000034
        mercury.rotation_y+=0.007
        venus.rotation_y+=0.0000017
        earth.rotation_y+=0.00041*100
        mars.rotation_y+=0.0004
        jupiter.rotation_y+=0.001
        saturn.rotation_y+=0.0022
        uranus.rotation_y+=0.00058
        neptune.rotation_y+=0.00062
        saturnRing.rotation_y+=0.5
        










    


    '''
    if player.intersects:
        player.y-=100 * time.dt
    '''



def input(key):
    global paused
    if held_keys['space']:
        player.y += 100 * time.dt
    if held_keys['control']:
        player.y -= 100 * time.dt









class Planet(Entity):

    def __init__(self, x, y, z, scale, texture):
        super().__init__()
        self.model = 'sphere'
        self.collider = 'sphere'
        self.x = x
        self.y = y
        self.z = z
        self.scale = scale
        self.shader = lit_with_shadows_shader
        self.texture = texture

        
        ### not sure about implementing ###
        self.speed_x=0
        self.speed_y=0
        self.speed_z=0


        self.sun = False




sun = Planet(0,0,0,100,'assets/8k_sun')
sun.sun=True






mercury=Planet(60,0,0,0.35035,'assets/mercury')
venus=Planet(70,0,0,0.8609,'assets/venus1')

earth=Planet(80,0,0,0.9159,'assets/earth')
earth.rotation_z=45

mars=Planet(90,0,0,0.4876,'assets/mars')
jupiter=Planet(110,0,0,10.2667,'assets/jupiter')
saturn=Planet(140,0,0,3.5562,'assets/saturn')
uranus=Planet(180,0,0,3.6704,'assets/uranus')
neptune = Planet(210,0,0,3.5562,'assets/neptune')



### MOONS ###
moon = Planet(80,2,0,0.05,'assets/Moon')



### TRUC ###
saturnRing=Entity(model="assets/saturnring.obj",
            shader = lit_with_shadows_shader,
            scale=1,
            parent=saturn,
            texture='assets/saturn_ring',
            position=(0, 0, 0),
            rotation=(0,0,23),
            collider='mesh'

            )




sky=Sky(texture="assets/space")
#EditorCamera()

player = FirstPersonController(model="sphere",
                               texture="assets/space",
                               position=(80, 0, 0),
                               gravity=0,
                               speed=100,
                               collider='sphere'
                               )

camera.clip_plane_far=909900


app.run()


