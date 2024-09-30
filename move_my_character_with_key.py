from pico2d import*

open_canvas()
tuk = load_image("TUK_GROUND.png")
horse = load_image('horse4.png')


running = True
#
def handle_events():
    global running
    global dir
    global udir

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                udir += 1
            elif event.key == SDLK_DOWN:
                udir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                udir -= 1
            elif event.key == SDLK_DOWN:
                udir += 1
#


x = 800 // 2
y = 600 // 4
frame = 0
dir = 0
udir = 0

while running:

    clear_canvas()
    tuk.draw(350, 300)
    horse.clip_draw(frame * 223, 0, 223, 160, x, y, 200, 144)
    update_canvas()
    handle_events()

    frame = (frame + 1) % 7

    if x== 710 or x == 90:
        break
    elif 90 < x < 710:
        x += dir * 4
        delay(0.04)
    if y == 550 or y == 50:
        break
    elif 50 < y < 550:
        y += udir * 4
        delay(0.04)




close_canvas()