import arcade
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


# blocchi #
class Brick():
    def __init__(self, x, y, contents=None):
        self.image = arcade.Sprite("images/block.png")
        self.image.center_x = x
        self.image.center_y = y
        self.contents = contents
        self.state = v.RESTING


    def update (self):
        if self.state == v.RESTING:
            self.resting()
        elif self.state == v.BUMPED:
            self.bumped()
        elif self.state == v.OPENED:
            self.opened()


    def setup_contents(self):
        if self.contents == '6coins':
            self.coin_total = 6
        else:
            self.coin_total = 0


    def resting(self): #quando non si muove
        if self.contents == '6coins':
            if self.coin_total == 0:
                self.state == v.OPENED


    def bumped(self): #quando viene colpito
        if self.contents == '6coins':
            if self.coin_total == 0:
                self.state = v.OPENED
            else:
                self.state = v.RESTING
        else:
            self.state = v.RESTING


    def opened(self): #quando viene aperto
        self.image = arcade.Sprite("images/coin.png")
