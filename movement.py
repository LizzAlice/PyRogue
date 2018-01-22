import tdl
# from settings import player_x, player_y
import settings

def handle_keys():


    keypress = False
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
            user_input = event
            keypress = True
    if not keypress:
        return

    # doesn't work
    # if user_input.key == 'ESCAPE' and user_input.alt:
    #     tdl.set_fullscreen(not tdl.get_fullscreen())
    if user_input.key == 'ESCAPE':
        return True #end game

    #movement keys
    if user_input.key == 'UP':
        settings.player_y -= 1
    elif user_input.key == 'DOWN':
        settings.player_y += 1
    elif user_input.key == 'LEFT':
        settings.player_x -= 1
    elif user_input.key == 'RIGHT':
        settings.player_x += 1
