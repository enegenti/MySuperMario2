import arcade
import Variabili as v


# blocchi #
class Brick():
    def __init__(self, contents=None, x, y):
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
