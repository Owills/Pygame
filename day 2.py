
import pygame

pygame.init()

bg = 0

def sayhello(p):
    print "hello", p

def makeNewRectangle():
    pygame.draw.rect(screen, bg, [x, y, rw, rh])



clock = pygame.time.Clock()

screenw = 700
screenh = 700

size = (screenw, screenw)
screen = pygame.display.set_mode(size)

rw = 50
rh = 50


x = 200
y = 300

xvel = 0
yvel = 0

white = (255, 255, 255)
bg = (255, 0, 0)
black = (0,0,0)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rw += 10
                makeNewRectangle()
            elif event.key == pygame.K_s:
                sayhello("Oliver")
                rw -= 10

            elif event.key == pygame.K_UP:
                yvel = -10
            elif event.key == pygame.K_DOWN:
                yvel = 10
            elif event.key == pygame.K_LEFT:
                xvel = -10
            elif event.key == pygame.K_RIGHT:
                xvel = 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                xvel = 0
            elif event.key == pygame.K_RIGHT:
                xvel = 0
            elif event.key == pygame.K_UP:
                yvel = 0
            elif event.key == pygame.K_DOWN:
                yvel = 0



    x += xvel
    y += yvel


    screen.fill(white)
    # print x, y

    pygame.draw.rect(screen, bg, [x, y, rw, rh])

    if x > screenw + rw:
        x = 0 - rw - 10

    if y > screenh - rh:
        y  = 0 - rh - 10

    if x < 0 - rw:
        x = screenw + rw

    if y < 0 - rh:
        y  = screenh + rh



    pygame.display.flip()


    clock.tick(20)



pygame.quit()