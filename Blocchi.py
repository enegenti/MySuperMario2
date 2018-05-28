import arcade
import Variabili as v


# blocchi #
class Brick():
    def __init__(self, x, y):
        self.sprite = arcade.Sprite("images/block.png")
        self.sprite.center_x = x
        self.sprite.center_y = y
        self.contents = contents

    def update (self):


    def get_image(self, x, y, width, height): # estrae l'immagine dal file
