# Overlay Interface for Rocket League

## Summary

After researching various libraries and tools for creating in-game overlays for Rocket League, **the most viable solution appears to be using the built-in rendering functionality provided by the RLBot framework**. The RLBot renderer offers a set of functions that allow for the creation of 2D and 3D graphics, text, and other visual elements within the game environment.

## Rendering Game Information

The RLBot renderer provides the following functions that can be used to display the state of the bot and other game-related information:

- `renderer.create_color(r, g, b, a)`
- `renderer.draw_rect_2d(x, y, width, height, color)`
- `renderer.draw_line_2d(x1, y1, x2, y2, color)`
- `renderer.draw_string_2d(x, y, scale_x, scale_y, color, text)`
- `renderer.draw_rect_3d(x, y, z, width, height, depth, color)`
- `renderer.draw_string_3d(x, y, z, scale_x, scale_y, color, text)`
- `renderer.draw_line_3d(x1, y1, z1, x2, y2, z2, color)`
- `renderer.draw_line_2d_3d(x1, y1, z1, x2, y2, z2, color)`

These functions can be used to create a custom overlay within the Rocket League game environment, displaying various information such as the bot's status, game scores, and other relevant data.

### Links

- [RLBot rendering Wiki](https://github.com/RLBot/RLBot/wiki/Rendering)
- [Python bot rendering example lines 59-62](https://github.com/RLBot/RLBotPythonExample/blob/master/src/bot.py)

## Clickable Overlays

Creating a fully interactive, clickable overlay within Rocket League would be a more complex task, as there is no dedicated solution for this functionality. Some potential approaches include using Python libraries like OpenCV, AutoGUI, IMGUI, or Tkinter. However, the development effort required for a clickable overlay **may not be worth the benefits**, as the built-in rendering capabilities of RLBot can provide a sufficient level of visualization and information display.

## FPS Meter

For monitoring the game's frame rate (FPS), the most straightforward solution is to use the built-in FPS counter provided by Rocket League. This can be enabled by going to the game's settings, navigating to the "Interface" tab, and enabling the "Performance Graphs" option, or use F10 hotkey. This will display the current FPS within the game window. Alternative could be to use Widows Game Bar.
