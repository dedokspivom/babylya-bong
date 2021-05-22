from pygame import *
from random import randint
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 50:
            self.rect.x += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 50:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 40, -15)
        bulletz.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y <= win_height:
            self.rect.y += self.speed 
        else:
            self.rect.y = 0
            self.rect.x = randint(80, win_width - 80)
            lost = lost + 1 

win_height = 500
win_width = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Догонялки хотя не бабуля")
background = transform.scale(image.load("dvorec.png"), (700, 500))
game = True 

speed_x = 3
speed_y = 3
clock = time.Clock()

back = (200, 255, 255)
window.fill(back)

score_left = 0
score_right = 0

font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)
win = font1.render("LEVUI игрок FUCKING SLAVE!", True, (255,255,255))
lose = font1.render("PRAVUI игрок FUCKING SLAVE!", True, (180, 0, 0))

FPS = 300

finish = False
game = True

Billy = Player('navalnui.jpg', 30, 200, 50, 100, 5)
Van = Player('navalnui.jpg', 620, 200, 50, 100, 5)
slave = GameSprite('tenis_ball.png', 350, 300, 25, 25, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False




    if finish != True:
        window.blit(background, (0, 0))
        window.fill(back)
        Billy.update_l()
        Van.update_r()
        slave.rect.x += speed_x
        slave.rect.y += speed_y

        if sprite.collide_rect(Billy, slave) or sprite.collide_rect(Van, slave):
            speed_x *= -1
        
        if slave.rect.y < 0 or slave.rect.y > win_height - 50:
            speed_y *= -1

        if slave.rect.x < 0 or slave.rect.x > win_height + 150:
            speed_x *= -1
        
        if slave.rect.x < 0:
            score_right = score_right + 1
            Billy = Player('navalnui.jpg', 30, 200, 50, 100, 5)
            Van = Player('navalnui.jpg', 620, 200, 50, 100, 5)
            slave = GameSprite('tenis_ball.png', 350, 300, 25, 25, 50)
           
        if slave.rect.x > win_width - 50:
            score_left = score_left + 1
            Billy = Player('navalnui.jpg', 30, 200, 50, 100, 5)
            Van = Player('navalnui.jpg', 620, 200, 50, 100, 5)
            slave = GameSprite('tenis_ball.png', 350, 300, 25, 25, 50)

        if score_right > 10:
            finish = True
            window.blit(win, (200,200))

        if score_left > 10:
            finish = True
            window.blit(lose, (200,200))

        text1 = font2.render("Счет", 1, (255, 255, 255))
        window.blit(text1, (350, 40))
        text2 = font2.render(str(score_left)+" : "+str(score_right), 1, (255, 255, 255))
        window.blit(text2, (350, 80))

        Billy.reset()
        Van.reset()
        slave.reset()
            
            
            

        display.update()
        clock.tick(FPS)
