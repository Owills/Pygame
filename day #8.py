import pygame
import random

pygame.init()

score = 0

clock = pygame.time.Clock()

screenw = 700
screenh = 700

size = (screenw, screenw)
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
bg = (255, 0, 0)
black = (0,0,0)
blue = (1, 164, 239)
orange = (240,147,17)

speed = 2

playerx = 10
playery = screenh/2

gap = 80

wall1hieght = random.uniform(gap, screenh-gap)
wall1width = 60
wall1x = screenw-wall1width
wall1y = screenh-wall1hieght

wall2hieght = random.uniform(gap, screenh-gap)
wall2width = 60
wall2x = (screenw-wall1width + screenw/2) - (screenw + wall1width / 2)
wall2y = screenh-wall1hieght

bulletx = -100
bullety = -100
numbullets = 3

wall1visible = True
wall2visible = True
w2visible = True
w1visible = True


vel = 3


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    vel = vel*-1
            elif event.key == pygame.K_DOWN:
                    vel = vel*1.5
            elif event.key == pygame.K_RIGHT:
                wall1x = wall1x - 20
                wall2x = wall2x - 20
            elif event.key == pygame.K_SPACE:
                if numbullets >0:
                    bulletx = playerx
                    bullety = playery
                    numbullets = numbullets -1
                else:
                    print "no more bullets"


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                    vel = abs(vel)
            elif event.key == pygame.K_DOWN:
                    vel = vel * 0.66






    screen.fill(black)

    if wall1visible == True:
        wall1 = pygame.draw.rect(screen, blue, [wall1x, wall1y, wall1width, wall1hieght])
    else:
        wall1 = pygame.draw.rect(screen, black, [wall1x, wall1y, wall1width, wall1hieght])
    if w1visible == True:
        w1 = pygame.draw.rect(screen, blue, [wall1x, 0, wall1width, screenh - wall1hieght - gap])
    else:
        w1 = pygame.draw.rect(screen, black, [wall1x, 0, wall1width, screenh - wall1hieght - gap])


    bullet = pygame.draw.rect(screen, orange, [bulletx, bullety, 5 , 4])

    if bulletx >=0 and bullety >=0:
        bulletx = bulletx +5


    if wall2visible == True:
        wall2 = pygame.draw.rect(screen, bg, [wall2x, wall2y, wall2width, wall2hieght])
    else:
        wall2 = pygame.draw.rect(screen, black, [wall2x, wall2y, wall2width, wall2hieght])

    if  w2visible == True:
        w2 =pygame.draw.rect(screen, bg, [wall2x, 0, wall2width, screenh - wall2hieght - gap])
    else:
        w2 =pygame.draw.rect(screen, black, [wall2x, 0, wall2width, screenh - wall2hieght - gap])

    player = pygame.draw.rect(screen, white, [playerx, playery, 20 , 20])
    playery = playery + vel

    if player.colliderect(wall1):
        if wall1visible == True:
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('Your Score Was: ' + str(score), True,white)
            screen.blit(text, [0, 350])
            pygame.display.flip()
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('Game Over', True,white)
            screen.blit(text, [350, 350])
            pygame.display.flip()
            pygame.time.wait(5000)
            done = True
        else:
            pass
    if player.colliderect(w1):
        if w1visible == True:
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('Your Score Was: ' + str(score), True,white)
            screen.blit(text, [0, 350])
            pygame.display.flip()
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('Game Over', True,white)
            screen.blit(text, [350, 350])
            pygame.display.flip()
            pygame.time.wait(5000)
            done = True
        else:
            pass
    if player.colliderect(wall2):
        if wall2visible == True:
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('Your Score Was: ' + str(score), True,white)
            screen.blit(text, [0, 350])
            pygame.display.flip()
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('Game Over', True,white)
            screen.blit(text, [350, 350])
            pygame.display.flip()
            pygame.time.wait(5000)
            done = True
        else:
            pass
    if player.colliderect(w2):
        if w2visible == True:
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('Your Score Was: ' + str(score), True,white)
            screen.blit(text, [0, 350])
            pygame.display.flip()
            font = pygame.font.SysFont('Times new roman', 30, True, True)
            text = font.render('Game Over', True,white)
            screen.blit(text, [350, 350])
            pygame.display.flip()
            pygame.time.wait(5000)
            done = True
        else:
            pass

    if bullet.colliderect(wall1) :
        wall1visible = False
        bulletx = -10
        bullety = -10
    if bullet.colliderect(w1):
        w1visible = False
        bulletx = -10
        bullety = -10
    if bullet.colliderect(wall2):
        wall2visible = False
        bulletx = -10
        bullety = -10
    if bullet.colliderect(w2):
        w2visible = False
        bulletx = -10
        bullety = -10




    wall1x = wall1x - speed
    wall2x = wall2x - speed


    if wall1x <= 0-wall1width:
        wall1x = screenw
        wall1hieght = random.uniform(gap, screenh-gap)
        wall1y = screenh-wall1hieght
        score = score + 1
        wall1visible = True
        w1visible = True



    if wall2x <= 0-wall2width:
        wall2x = screenw
        wall2hieght = random.uniform(gap, screenh-gap)
        wall2y = screenh-wall2hieght
        score = score + 1
        speed = speed + 0.1
        wall2visible = True
        w2visible = True



    font = pygame.font.SysFont('Times new roman', 30, True, True)
    text = font.render('Score: ' + str(score), True,white)
    screen.blit(text, [0, 0])





    font = pygame.font.SysFont('Times new roman', 30, True, True)
    text = font.render('Number of bullets: ' + str(numbullets), True,white)
    screen.blit(text, [400,0])





    pygame.display.flip()


    clock.tick(60)

pygame.quit()
