#IMPORT
import arcade

#VAR
MOVEMENT_SPEED = 4
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Super Mario Bros 1-1"

# COLORS #
#               R    G    B
GRAY         = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
WHITE        = (255, 255, 255)
RED          = (255,   0,   0)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE

SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

#Brick and coin box contents#

MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

FIREBALL = 'fireball'

#BRICK STATES

RESTING = 'resting'
BUMPED = 'bumped'

#COIN STATES
OPENED = 'opened'
#
# blocchi #
class Brick():
    def __init__(self, x, y):
        self.sprite = arcade.Sprite("Graphics/block.png", 0.2)
        self.sprite.center_x = x
        self.sprite.center_y = y


    def draw(self):
        self.sprite.draw()


    def update(self, dt):
        self.sprite.center_y += 4 * dt * 60
        if self.sprite.center_y > 520:
            self.sprite.center_y = -30


    def update (self):
        if self.state == RESTING:
            self.resting()
        elif self.state == BUMPED:
            self.bumped()
        elif self.state == OPENED:
            self.opened()


    def setup_contents(self):
        if self.contents == '6coins':
            self.coin_total = 6
        else:
            self.coin_total = 0


    def resting(self): #quando non si muove
        if self.contents == '6coins':
            if self.coin_total == 0:
                self.state == OPENED


    def bumped(self): #quando viene colpito
        if self.contents == '6coins':
            if self.coin_total == 0:
                self.state = OPENED
            else:
                self.state = RESTING
        else:
            self.state = RESTING


    def opened(self): #quando viene aperto
        self.image = arcade.Sprite("Graphics/coin.png")


class MyWindow(arcade.Window):
    def __init__(self, breite, hoehe, titel):
        super().__init__(breite, hoehe, titel)
        arcade.set_background_color((0, 0, 0))

        self.mario = arcade.Sprite("Graphics/mario_f_1.png", 0.1)
        self.brick1 = Brick(100,100)



        self.mario.x = 20
        self.mario.y = 20
        self.w = 32
        self.h = 32
        self.delta_y = 0
        self.delta_x = 0

        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        for x in range(100, 650, 10):
            wall = arcade.Sprite("Graphics/coin.png", 0.1)
            wall.center_x = x
            wall.center_y = 10
            self.all_sprites_list.append(wall)
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.mario, self.wall_list)

    def on_draw(self):
        arcade.start_render()
        self.mario.draw()
        self.brick1.draw()
        self.wall_list.draw()


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.delta_y= 15
        elif key == arcade.key.DOWN:
            self.delta_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.delta_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.delta_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):  # Taste losgelassen
        if (key == arcade.key.LEFT or key == arcade.key.RIGHT):
            self.delta_x = 0

    def update(self, dt):

        if self.physics_engine.update() and self.delta_x>0:
            self.delta_x=-10
        elif self.physics_engine.update() and self.delta_x<0:
            self.delta_x=10
        self.mario.center_x = self.mario.x
        self.mario.center_y = self.mario.y

        self.delta_y -= 1.15
        self.mario.x += self.delta_x*2
        self.mario.y += self.delta_y
        if self.mario.x >= 1200:
            self.mario.x = 1200
        if self.mario.y >= 1000:
            self.mario.y = 1000
        if self.mario.y <= 30:
            self.mario.y = 30
        if self.mario.x <= 16:
            self.mario.x = 16


window = MyWindow(800, 600, "Klassen")
arcade.run()
