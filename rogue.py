import tdl

from movement import handle_keys
import settings as s



tdl.set_font('celtic_garamond_10x10_gs_tc.png', greyscale=True, altLayout=True)

console = tdl.init(s.SCREEN_WIDTH, s.SCREEN_HEIGHT, title="PyRogue", fullscreen = False)
tdl.set_fps(s.LIMIT_FPS)

while not tdl.event.is_window_closed():
    console.draw_char(s.player_x,s.player_y,'a', bg=None, fg=(255,255,255))

    exit_game = handle_keys()
    if exit_game:
        break

    tdl.flush() #always execute at end of loop; presents changes to screen
