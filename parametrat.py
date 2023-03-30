
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
        if keys[K_s] and self.rect.y < 600:
            self.rect.y += self.speed 
    def update1(self):
        keys = key.get_pressed()
        if keys[K_i] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_k] and self.rect.y < 600:
            self.rect.y += self.speed 

ww = 800
wh = 600
win = display.set_mode((ww,wh))
back = transform.scale(image.load(img_back), (ww,wh))
p1 = Player(img_hero,0,6,10,120,120)
p2 = Player(img_hero,680,6,10,120,120)
ball = Player(img_ball,370,-20,10,60,60)


finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        win.blit(back,(0,0))
        p2.reset()
        p1.reset()
        ball.reset()
        p1.update()
        p2.update1()
        ball.update()

       

    display.update()
    clock.tick(fps)
