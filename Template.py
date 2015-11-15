import pygame

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

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    pygame.display.flip()


    clock.tick(60)

pygame.quit()
