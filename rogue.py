import tdl

from movement import handle_keys
import settings as s



tdl.set_font('celtic_garamond_10x10_gs_tc.png', greyscale=True, altLayout=True)

root = tdl.init(s.SCREEN_WIDTH, s.SCREEN_HEIGHT, title="PyRogue", fullscreen = False)
con = tdl.Console(s.SCREEN_WIDTH, s.SCREEN_HEIGHT)

tdl.set_fps(s.LIMIT_FPS)

while not tdl.event.is_window_closed():
    con.draw_char(s.player_x,s.player_y,'a', bg=None, fg=(255,255,255))

    tdl.flush() #always execute at end of loop; presents changes to screen

    con.draw_char(s.player_x, s.player_y, ' ', bg=None )
    exit_game = handle_keys()
    if exit_game:
        break
