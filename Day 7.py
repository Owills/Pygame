import pygame

pygame.init()

clock = pygame.time.Clock()

screenw = 700
screenh = 700

rw = 50
rh = 50

x = 200
y = 300

size = (screenw, screenw)
screen = pygame.display.set_mode(size)

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
            pass

            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                x = x - 10


    Player = pygame.draw.rect(screen, blue, [x, y, rw, rh])
    wall = pygame.draw.rect(screen, blue, [x+100, y-150, rw, 2*rh])
    wall2 = pygame.draw.rect(screen, blue, [x+100, y+150, rw, 2*rh])



    pygame.display.flip()


    clock.tick(60)

pygame.quit()
