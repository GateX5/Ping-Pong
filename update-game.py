from pygame import *

clock = time.Clock()
fps = 60
img_ball = "ball1.png"
img_hero = "paddle1.png"
img_back = "table.jpg"

class Game(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,speed,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(Game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 800:
            self.rect.y += self.speed 
    def update1(self):
        keys = key.get_pressed()
        if keys[K_i] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < 800:
            self.rect.y += self.speed 

  
ww = 800
wh = 600
win = display.set_mode((ww,wh))
back = transform.scale(image.load(img_back), (ww,wh))
p1 = Player(img_hero,30,250,10,10,50)
p2 = Player(img_hero,780,250,10,10,50)
ball = Player(img_ball,370,235,10,60,60)
speed_x = 3
speed_y = 3
score = 0 
score2 = 0
score_max = 2

font.init()
font = font.Font(None,35)
l1= font.render("player 1 lose",True ,(100,0,0))
l2 = font.render("player 2 lose",True ,(100,0,0))
l3 = font.render("player 1 win",True ,(100,120,90))
l4 = font.render("player 2 win",True ,(100,120,90))


finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish: 
        win.blit(back,(0,0))

        text = font.render("Score: " + str(score), 1, (255, 255, 255))
        win.blit(text, (30, 0))
        
        text1 = font.render("Score: " + str(score2), 1, (255, 255, 255))
        win.blit(text1, (700, 0))

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if ball.rect.y > wh-50 or ball.rect.y < 0:
            speed_y *= -1
        
        if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2,ball):
            speed_y *= 1
            speed_x *= -1
        
        if ball.rect.x < 0:
           score2 += 1
           ball = Player(img_ball,370,235,10,60,60)

        if score == 2:
            win.blit(l2,(450, 150))
            win.blit(l3,(100, 150))
            finish = True
            
        
        if ball.rect.x > ww:
            score += 1
            ball = Player(img_ball,370,235,10,60,60)
        
        if score2 == 2:
            win.blit(l1,(450, 150))
            win.blit(l4,(100, 150))
            finish = True
       
        p2.reset()
        p1.reset()
        ball.reset()
        p1.update()
        p2.update1()

   
    clock.tick(fps)
    display.update()
