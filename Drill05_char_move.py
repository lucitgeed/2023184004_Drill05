from pico2d import*

open_canvas()
tuk = load_image("TUK_GROUND.png")
horse = load_image('horse4.png')

frame = 0
for x in range(0, 800, 10):
    clear_canvas()
    tuk.draw(350, 300)
    horse.clip_draw(frame* 223, 0, 223, 160, x, 90)
    update_canvas()
    frame = (frame + 1) % 7
    delay(0.05)




running = True

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False








close_canvas()