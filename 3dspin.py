
import pyglet
from pyglet.gl import *
from pyglet import clock

class Hud(object):
    def __init__(self, win):
        self.text = pyglet.text.Label(
            # helv,
            'Let it spin..',
            font_size=40,
            x=win.width / 2,
            y=win.height / 2,
            anchor_x='center', anchor_y='center',
            color=(255,255,255,255),
        )
        
    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.text.draw()

def callback(dt):
    global rot_y, pos
    rot_y += 5
    # print("rotating on the y axis")

pos = [0, 0, -20]
# default angle 
rot_y = 45
win = pyglet.window.Window(height=500, width=500)
hud = Hud(win)
clock.schedule_interval(callback, 0.01)

@win.event
def on_draw():
    global pos_z, rot_y
    win.clear()
    # Make the text in front of the shape
    glEnable(GL_DEPTH_TEST)
    # if you want to keep three sides drawn in the 3rd space only
    # glEnable(GL_CULL_FACE)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, win.width, 0, win.height)
    hud.draw()
    # glDisable(GL_TEXTURE_2D)
    # different color for the shape
    glColor3f(0.7, 0.2, 0.3)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # setup projection matrix
    # load perspective matrix
    gluPerspective(140, 1, 10, 500)
    # modelview for objection transformation
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # moving the objects to a new position
    glTranslatef(*pos)
    # multiple by the rotation matrix
    # left and right keys
    glRotatef(rot_y, 0, 1, 0)
    # filling a polygon "square"
    glBegin(GL_POLYGON)
    # bottom left
    glVertex3f(-10,-10,0)
    # bottom right
    glVertex3f(10,-10,0)
    # top right
    glVertex3f(10,20,0)
    # top left
    glVertex3f(-10,20,0)
    glEnd()
    glFlush()
    

@win.event
def on_key_press(s,m):
    global pos_z, rot_y
    if s == pyglet.window.key.W:
        pos[2] -= 1
    if s == pyglet.window.key.S:
        pos[2] += 1
    if s == pyglet.window.key.A:
        rot_y += 5
    if s == pyglet.window.key.D:
        rot_y -= 5

pyglet.app.run()
