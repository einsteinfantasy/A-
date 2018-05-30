import pygame
import random

width = 800
height = 600
display_size = (width, height)
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption('A*')
pygame.mouse.set_cursor(*pygame.cursors.diamond)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)


class Block():
    def __init__(self, x, y, length=20):
        self.length = length
        self.xmax = width / length - 1
        self.ymax = height / length - 1
        self.centerx = x * length + length / 2
        self.centery = (self.ymax - y) * length + length / 2
        self.mom = None
        self.g = 0
        self.h = 0
        self.f = 0
        self.x = x
        self.y = y
        self.avai = True

    def update(self):
        self.h = abs(x_in - self.x) + abs(y_in - self.y)
        if i == 1 or i == 3 or i == 7:
            self.g = 1.4
        else:
            self.g = 1
        self.f = self.g + self.h

    def printpath(self):
        start_block0.mom = start_block0
        while self != start_block0:
            print(self.centerx, self.centery)
            pygame.draw.circle(screen, green, (int(self.centerx), int(self.centery)), 10)
            pygame.display.flip()
            self = self.mom


screenmap = [[]]

for i in range(40):
    screenmap[i] = []
    for j in range(30):
        block = Block(i, j)
        screenmap[i].append(block)
    screenmap.append(screenmap[i])
open_list = []
close_list = []
b = True


for obs in range(500):
    ob_x = random.randint(0, 39)
    ob_y = random.randint(0, 29)
    ob = screenmap[ob_x][ob_y]
    ob.avai = False
    pygame.draw.rect(screen, red, (ob.centerx-10, ob.centery-10, 14, 14))
    pygame.display.flip()


start_x = random.randint(0, 39)
start_y = random.randint(0, 29)
start_block = screenmap[start_x][start_y]
pygame.draw.rect(screen, white, (start_block.centerx, start_block.centery, 14, 14))
pygame.display.flip()

while b:
    global a
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            a = pygame.mouse.get_pos()
            b = False
pygame.draw.rect(screen, white, (a[0], a[1], 10, 10))
pygame.display.flip()
global x_in, y_in
x_in = int(a[0] / 20)
y_in = int((height - a[1]) / 20)
target_block = screenmap[x_in][y_in]


start_block.update()
# pygame.draw.rect(screen, white, (start_block.centerx, start_block.centery, 10, 10))
open_list.append(start_block)
start_block0 = start_block
while True:
    open_list.sort(key=lambda block: block.f)
    start_block = open_list[0]
    open_list.remove(start_block)
    close_list.append(start_block)
    around = [
        [start_block.x, start_block.y + 1],  # up
        [start_block.x + 1, start_block.y + 1],  # upright
        [start_block.x + 1, start_block.y],  # right
        [start_block.x + 1, start_block.y - 1],  # downright
        [start_block.x, start_block.y - 1],  # down
        [start_block.x - 1, start_block.y - 1],  # downleft
        [start_block.x - 1, start_block.y],  # left
        [start_block.x - 1, start_block.y + 1],  # upleft
    ]
    for i in range(8):
        next_x = around[i][0]
        next_y = around[i][1]
        if around[i][0] == -1 or around[i][1] == -1 or around[i][0] == 40 or around[i][1] == 30:
            continue
        next_block = screenmap[next_x][next_y]
        if next_block not in close_list and next_block.avai == True:
            if next_block == target_block:
                next_block.mom = start_block
                print('find')
                next_block.printpath()
                pygame.time.delay(1400)
                exit()
            elif next_block in open_list:
                copy = next_block
                copy.update()
                if copy.f < next_block.f:
                    next_block.update()
                continue
            next_block.update()
            open_list.append(next_block)
            next_block.mom = start_block
