import pygame

bg = (255, 255, 255)
red = (243, 81, 35)
blue = (1, 164, 239)
yellow = (255, 185, 1)
green = (127, 186, 0)
x = 400

pygame.init()

size = (700, 700)
screen = pygame.display.set_mode(size)

done = False

clock = pygame.time.Clock()


spacelen = 20

redstart = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    w = 350
    l = 350


    screen.fill(bg)

    pygame.draw.rect(screen, red, [redstart - spacelen/2, 0 - spacelen/2, w, l])
    pygame.draw.rect(screen, green, [350 + spacelen/2, 0 - spacelen/2, w, l])
    pygame.draw.rect(screen, blue, [0 - spacelen / 2, 350 + spacelen / 2, w, l])
    pygame.draw.rect(screen, yellow, [350 + spacelen/2, 350 + spacelen/2, w, l])

   # redstart += 30
    spacelen += 10

    if spacelen == x:
        spacelen = spacelen - 700
        x = x - 50
    if x == 50:
        x = x + 400



    font = pygame.font.SysFont('Times new roman', 30, True, True)
    text = font.render('microsoft', True, yellow )
    screen.blit(text, [350, 350])




    pygame.display.flip()


    clock.tick(20)



pygame.quit()