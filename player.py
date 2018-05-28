import arcade
import var

class Player(arcade.Sprite):
    def __init__(self, x, y):
        self.sprite = arcade.Sprite("Graphics/mario_f_1.png")
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.playerx = 400
        self.playery = 300


    def draw(self):
        self.sprite.draw()


    def update(self, dt):
        self.sprite.center_x = self.playerx
        self.sprite.center_y = self.playery

        self.playerx += self.vx * 2
        self.playery += self.vy * 2

