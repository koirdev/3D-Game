from ursina import *
from config import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

def input(key):
	if key == 'left mouse down':
		Audio('assets/sounds/shot.wav')



app = Ursina(
	title='3D-GAME',
	fullscreen=True,
	development_mode=True,
	show_ursina_splash=False
	)

# Render objects
enemy = Entity(model="assets/3d_models/enemy.glb", scale=2, x=0, y=2, shader=lit_with_shadows_shader)
cube1 = Entity(model="cube",color=color.red, texture="white_cube", scale=1, x=7, y=0.5, collider='box', shader=lit_with_shadows_shader)
cube2 = Entity(model="cube",color=color.red, texture="white_cube", scale=1, x=5, y=2, collider='box', shader=lit_with_shadows_shader)
cube3 = Entity(model="cube",color=color.red, texture="white_cube", scale=1, x=3, y=4, collider='box', shader=lit_with_shadows_shader)
ground = Entity(model='plane',texture='assets/images/grass_tex.png',collider='mesh',scale=(100,1,100),texture_scale=(100,100), shader=lit_with_shadows_shader)
floor = Entity(model='cube',texture='white_cube',collider='box',scale=(5,0.2,5),x=0, y=4.3,shader=lit_with_shadows_shader)
wall1 = Entity(model='cube',texture='white_cube',collider='box',scale=(0.5,3,5),x=-2.2, y=5.9,shader=lit_with_shadows_shader)
wall2 = Entity(model='cube',texture='white_cube',collider='box',scale=(4.5,3,0.4),x=0.2, y=5.9,z=-2.3,shader=lit_with_shadows_shader)
wall3 = Entity(model='cube',texture='white_cube',collider='box',scale=(4.5,3,0.4),x=0.2, y=5.9,z=2.3,shader=lit_with_shadows_shader)
wall4 = Entity(model='cube',texture='white_cube',collider='box',scale=(0.5,3,2),x=2.2, y=5.9,z=-1.5,shader=lit_with_shadows_shader)
wall5 = Entity(model='cube',texture='white_cube',collider='box',scale=(0.5,3,2),x=2.2, y=5.9,z=1.5,shader=lit_with_shadows_shader)
wall6 = Entity(model='cube',texture='white_cube',collider='box',scale=(0.6,1,1),x=2.2, y=6.9,z=-0.01,shader=lit_with_shadows_shader)
door = Entity(model='cube',texture='assets/images/door_tex.png',scale=(0.7,2,1),x=2.2, y=5.5, z=-0.01,shader=lit_with_shadows_shader)
gun = Entity(model="assets/3d_models/gun.glb", scale=0.9,color=color.red,texture='white_cube',parent=camera.ui,rotation=(0,-70,0),position=(0.5,-0.2,3),shader=lit_with_shadows_shader)
#house1 = Entity(model="assets/3d_models/house1.glb", scale=0.5, x=10, y=0.1,z=15,collider='box',rotation=(0,450,0),position=(40,0,40),shader=lit_with_shadows_shader)

# View Mode text
if VIEW_MODE == 1:
	text_entity = Text('VIEW_MODE',scale=2,x=-00.1,y=0.5)
else:
# Version Text
	text_entity = Text('ver. 0.1',scale=2,x=-00.1,y=0.5)
table = Entity(model="cube",color=color.brown, texture="white", scale=(1,1,3), x=-1.5, y=5, collider='box', shader=lit_with_shadows_shader)
Sky(texture='assets/images/sky_tex.png', shader=lit_with_shadows_shader)


# Shaders
light = DirectionalLight(shadows=True)
light.look_at(Vec3(1,-1,1))

# Rotating objects
def update():
	enemy.rotation_x = enemy.rotation_x + 0.25
	enemy.rotation_y = enemy.rotation_y + 0.5
	gun.rotation_y = gun.rotation_y + 0.5
	if VIEW_MODE == 1:
		text_entity.rotation_y = text_entity.rotation_y + 0.9


# View Mode
if VIEW_MODE == 1:
	EditorCamera()

	#player = FirstPersonController(speed = 7,model='cube', jump_height = 2.2, jump_up_duration = 0.7,x=10,mouse_sensitivity = Vec2(MOUSE_SENS, MOUSE_SENS), cursor = Entity(parent=camera.ui, model='circle', color=color.white, scale=0.01, ))

if VIEW_MODE == 0:
# Player
	player = FirstPersonController(speed = 7,collider='box', jump_height = 2.2, jump_up_duration = 0.7,x=10,shader=lit_with_shadows_shader, cursor = Entity(parent=camera.ui, model='circle', color=color.white, scale=0.01, ))



app.run()
