
import pygame
import random

pygame.init()


score = 0

clock = pygame.time.Clock()

screenw = 700
screenh = 700

size = (screenw, screenw)
screen = pygame.display.set_mode(size)


enemyList = [
    [0,0],
    [100,100]
]

rw = 50
rh = 50


x = 200
y = 300

cx = 350
cy = 350

cxv = random.random() * 20
cyv = random.random() * 20

xvel = 0
yvel = 0

white = (255, 255, 255)
bg = (255, 0, 0)
black = (0,0,0)
blue = (1, 164, 239)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rw += 10

            elif event.key == pygame.K_s:

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


    print enemyList

    x += xvel
    y += yvel


    screen.fill(bg)

    timer = (pygame.time.get_ticks()/1000)

    player = pygame.draw.rect(screen, blue, [x, y, rw, rh])

    computer = pygame.draw.rect(screen, black, [cx, cy, rw, rh])

    if player.colliderect(computer):
        player = pygame.draw.rect(screen, black, [x, y, rw, rh])
        score += 1
        cx = random.random() * (screenw - rw)
        cy = random.random() * (screenh - rh)
        cxv = random.random() * 20
        cyv = random.random() * 20


    cx += cxv
    cy += cyv


    font = pygame.font.SysFont('Times new roman', 30, True, True)
    text = font.render('Score: ' + str(score), True, black )
    screen.blit(text, [0, 0])


    font = pygame.font.SysFont('Times new roman', 30, True, True)
    text = font.render('Time: ' + str(timer) , True, black )
    screen.blit(text, [500, 670])



    if x <= 0:
        x = 0
        xvel = 0
    if y <= 0:
        y = 0
        yvel = 0
    if x >= screenw - rw:
        x = screenw - rw
    if y >= screenh - rh:
        y = screenh - rh


    if cx <= 0 or  cx >= screenw - rw:
        cxv = cxv * -1
    if cy <= 0 or cy >= screenh - rh:
        cyv = cyv * -1




    pygame.display.flip()


    clock.tick(60)

    if timer == 30:

        if score >= 20:
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('You win!', True, black )
            screen.blit(text, [100, 350])
            pygame.display.flip()

        else:
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('You lose!', True, black )
            screen.blit(text, [100, 350])
            pygame.display.flip()

        pygame.time.wait(1000)
        done = True





pygame.quit()