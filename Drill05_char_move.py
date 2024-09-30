from pico2d import*

open_canvas()

horse = load_image('horse4.png')

frame = 0
for x in range(0, 800, 10):
    clear_canvas()
    horse.clip_draw(frame* 223, 0, 223, 160, x, 90)
    update_canvas()
    frame = (frame + 1) % 7
    delay(0.05)

close_canvas()