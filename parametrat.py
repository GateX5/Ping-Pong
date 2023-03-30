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
