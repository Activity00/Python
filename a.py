import pygame
import random
import time

# from pygame.examples.video import clock

pygame.init()

size = (1918, 926)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("snow")
# 加载位图
background = pygame.image.load('timg1.jpg')

snow = []
for i in range(300):
    x = random.randrange(0, size[0])
    y = random.randrange(0, size[1])
    speedx = random.randint(-1, 2)
    speedy = random.randint(3, 8)
    snow.append([x, y, speedx, speedy])

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))

    for i in range(len(snow)):
        pygame.draw.circle(screen, (255, 255, 255), snow[i][:2], snow[i][3])
        snow[i][0] += snow[i][2]
        snow[i][1] += snow[i][3]

        if snow[i][1] > size[1]:
            snow[i][1] = random.randrange(-50, -10)
            snow[i][0] = random.randrange(0, size[0])

    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(20)

pygame.quit()
