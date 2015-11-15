
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
red = (255, 0, 0)
blue = (1, 164, 239)
blue = (1, 164, 239)

done = False

squareList = []

def makeNewSquare(screen, x,y ):
    newSquare = pygame.draw.rect(screen, blue ,[x,y,50,50])
    xvel = 10
    yvel = 10
    squareList.append(newSquare)

def moveSquare(square):
    print square.x,square.y,square.h,square.w

    square.x = square.x + 30

    def draw(square):
        pygame.draw.rect(screen, blue, [square.x, square.y, square.w, square.h])

    draw(square)
    # return square





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                makeNewSquare(screen, random.random() * screenw, random.random() * screenw)


    # print pygame.mouse.get_pos()[0]


    # squareList[0] = moveSquare(squareList[0])
    for s in squareList:
        moveSquare(s)


    print squareList


    pygame.display.flip()


pygame.quit()