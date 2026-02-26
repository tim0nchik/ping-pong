from pygame import *

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800

window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('ping-pong')

timer = time.Clock()


game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255,255,255))

    display.update()
    timer.tick(60)