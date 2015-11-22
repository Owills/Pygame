
import pygame
import random

pygame.init()


score = 0

clock = pygame.time.Clock()

screenw = 700
screenh = 700

size = (screenw, screenw)
screen = pygame.display.set_mode(size)




rw = 50
rh = 50

wrw = rw
wrh = rh


x = 300
y = 300




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
            if event.key == pygame.K_UP:
                wrh = wrh -10
            elif event.key == pygame.K_DOWN:
                wrh =  wrh + 10
            elif event.key == pygame.K_LEFT:
                wrw = wrw - 10
            elif event.key == pygame.K_RIGHT:
                wrw = wrw + 10






    screen.fill(bg)

    timer = (pygame.time.get_ticks()/1000)

    player = pygame.draw.rect(screen, blue, [y, x, rw, rh])

    wall = pygame.draw.rect(screen, black, [screenw-wrw,0, wrw, x])
    wall2 = pygame.draw.rect(screen, black, [screenw-wrw, x+rw,wrw,screenw-x])











    pygame.display.flip()


    clock.tick(60)








pygame.quit()