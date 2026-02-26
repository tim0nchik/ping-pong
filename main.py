from pygame import *

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 800

window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption('ping-pong')

timer = time.Clock()


game = True

class Gamesprite(sprite.Sprite):
    def __init__(self, image_, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def __init__(self, image_, x, y, width, height, speed, key_up, key_down):
        super().__init__(image_, x, y, width, height, speed)
        self.key_up = key_up
        self.key_down = key_down

    def update(self):
        keys = key.get_pressed()
        
        if keys[self.key_down] and self.rect.y <= WINDOW_HEIGHT-self.rect.height:
            self.rect.y += self.speed
        if keys[self.key_up] and self.rect.y >= 0:
            self.rect.y -= self.speed
    


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255,255,255))

    display.update()
    timer.tick(60)