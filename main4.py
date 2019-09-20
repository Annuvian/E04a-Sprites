#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)

        self.character_list = arcade.SpriteList()


    def setup(self):
        x = 100
        y = 300
        characters = ["gary", "kk", "krabs", "patrick", "pearl", "plankton", "puff", "sandy", "spongebob", "squidward"]
        for i in range(10):
            character = characters[i]
            self.character_sprite = arcade.Sprite("images/{character}.png".format(character=character), 0.4)
            self.character_sprite.center_x = x
            self.character_sprite.center_y = y
            x = x + 250
            if x >= 700:
                x = 100
                y = y + 200
            self.character_list.append(self.character_sprite)

    def on_draw(self):
        arcade.start_render()
        self.character_list.draw()


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        self.character_sprite.center_x = x
        self.character_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.set_background_color(open_color.black);

    def on_mouse_release(self, x, y, button, modifiers):
        arcade.set_background_color(open_color.white);
        

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()