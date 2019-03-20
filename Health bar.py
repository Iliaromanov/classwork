import arcade


WIDTH = 640
HEIGHT = 480

max_health = 100
current_health = 40

def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...

    width = current_health / max_health * 300

    arcade.draw_text(f"{current_health}/{max_health}", 160, 300, arcade.color.BLACK_OLIVE)
    arcade.draw_xywh_rectangle_filled(160, 240, 300, 40, arcade.color.BLACK_OLIVE)
    arcade.draw_xywh_rectangle_filled(160, 240, width, 40, arcade.color.BANGLADESH_GREEN)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
