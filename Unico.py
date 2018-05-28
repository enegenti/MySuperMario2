import arcade
import time

MOVEMENT_SPEED = 4

class MyWindow(arcade.Window):
    def __init__(self, breite, hoehe, titel):
        super().__init__(breite, hoehe, titel)
        arcade.set_background_color((0, 0, 0))

        self.mario = arcade.Sprite("Graphics/mario_f_1.png", 0.1)


        self.mario.x = 320
        self.mario.y = 240
        self.w = 32
        self.h = 32
        self.delta_y = 0
        self.delta_x = 0

    def on_draw(self):
        arcade.start_render()
        self.mario.draw()


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
        self.mario.center_x = self.mario.x
        self.mario.center_y = self.mario.y

        self.delta_y -= 1
        self.mario.x += self.delta_x*2
        self.mario.y += self.delta_y
        if self.mario.x >= 624:
            self.mario.x = 624
        if self.mario.y >= 464:
            self.mario.y = 464
        if self.mario.y <= 30:
            self.mario.y = 30
        if self.mario.x <= 16:
            self.mario.x = 16


window = MyWindow(800, 600, "Klassen")
arcade.run()
