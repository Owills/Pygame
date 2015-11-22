import pygame
import random

pygame.init()

clock = pygame.time.Clock()

screenw = 700
screenh = 700

size = (screenw, screenw)
screen = pygame.display.set_mode(size)

white = (255, 255, 255)
bg = (255, 0, 0)
black = (0,0,0)
blue = (1, 164, 239)

gap = 80

wall1hieght = random.random()*screenh-gap
wall1width = 60
wall1x = screenw-wall1width
wall1y = screenh-wall1hieght

wall2hieght = random.random()*screenh-gap
wall2width = 60
wall2x = (screenw-wall1width + screenw/2) + (screenw + wall1width / 2)
wall2y = screenh-wall1hieght



done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill(black)

    wall1 = pygame.draw.rect(screen, blue, [wall1x, wall1y, wall1width, wall1hieght])

    pygame.draw.rect(screen, blue, [wall1x, 0, wall1width, screenh - wall1hieght - gap])



    wall2 = pygame.draw.rect(screen, bg, [wall2x, wall2y, wall2width, wall2hieght])

    pygame.draw.rect(screen, bg, [wall2x, 0, wall2width, screenh - wall2hieght - gap])


    wall1x = wall1x - 5
    wall2x = wall2x -5

    if wall1x <= 0-wall1width:
        wall1x = screenw
        wall1hieght = random.random()*screenh-gap
        wall1y = screenh-wall1hieght

        print "blue" , wall1hieght

    if wall2x <= 0-wall2width:
        wall2x = screenw
        wall2hieght = random.random()*screenh-gap
        wall2y = screenh-wall2hieght

        print "red" , wall2hieght





    pygame.display.flip()


    clock.tick(60)

pygame.quit()
