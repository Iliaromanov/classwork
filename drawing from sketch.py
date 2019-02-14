import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
# Begin drawing

#sun
arcade.draw_circle_filled(-100, -100, 50, arcade.color.BRONZE_YELLOW)

# Grass
arcade.draw_rectangle_filled(0, 0, 1300, 100, arcade.color.APPLE_GREEN)

# First tree bottom
arcade.draw_rectangle_filled(200, 85.5, 20, 75, arcade.color.ANTIQUE_BRONZE)

# First tree top
arcade.draw_triangle_filled(160, 125, 240, 125, 200, 200, arcade.color.BANGLADESH_GREEN)

# End drawing
arcade.finish_render()
arcade.run()