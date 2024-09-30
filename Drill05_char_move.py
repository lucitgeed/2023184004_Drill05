from pico2d import*

open_canvas()
tuk = load_image("TUK_GROUND.png")
horse = load_image('horse4.png')


running = True
#
def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
#

x = 800 // 2
frame = 0
dir = 0
while running:
    clear_canvas()
    tuk.draw(350, 300)
    horse.clip_draw(frame* 223, 0, 223, 160, x, 90)
    update_canvas()

    handle_events()
#    if not running:
#       break

    frame = (frame + 1) % 7
    delay(0.05)


close_canvas()