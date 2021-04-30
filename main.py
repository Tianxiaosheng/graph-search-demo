import pygame
import queue
from tkinter import *
from tkinter import messagebox
import random


def makeObstacle(surface, s, cell_num, pos):

    dist = s//cell_num

    lX = 0
    lY = 0

    for p in range(cell_num):
        for q in range(cell_num):
            area = pygame.Rect(lX, lY, dist, dist)
            if area.collidepoint(pos):
                # print(pos)
                if surface.get_at(pos)[0:3] == (180, 110, 255):
                    pygame.draw.rect(surface, (0, 0, 0), (lX, lY, dist, dist))
                    pygame.draw.rect(surface, (0, 255, 255),
                                     (lX, lY, dist, dist), 1)
                else:
                    pygame.draw.rect(surface, (180, 110, 255),
                                     (lX, lY, dist, dist))
                pygame.display.update()
                return
            lX = lX + dist
        lX = 0
        lY = lY + dist

def randomMatrix(surface, s, cell_num):
 
    dist = s//cell_num

    for m in range(dist):
        x = random.randint(0, s-1)
        y = random.randint(0, s-1)
        print(x,y)
        makeObstacle(surface, s, cell_num, (x, y))


def makeMaze(surface, s, cell_num):

    dist = s//cell_num

    lX = 0
    lY = 0

    for p in range(cell_num):
        for q in range(cell_num):
            pygame.draw.rect(surface, (0, 255, 255), (lX, lY, dist, dist), 1)
            lX = lX + dist
        lX = 0
        lY = lY + dist

    pygame.display.update()


def Breadth_First_Algorithm(surface, screen_width, cell_num):

    cell_width = screen_width//cell_num

    start = (0, 0)
    finish = (screen_width - cell_width, screen_width - cell_width)

    sXX = start[0]
    sYY = start[1]

    pygame.draw.rect(surface, (0, 0, 255), (start, (cell_width, cell_width)))
    pygame.draw.rect(surface, (0, 255, 0), (finish, (cell_width, cell_width)))

    pygame.display.update()

    sX = sXX + (cell_width//2)
    sY = sYY + (cell_width//2)

    path = queue.Queue()
    add = "S"
    path.put(add)
    print("")
    while True:

        k = 0
        add = path.get()
        print(add)

        X = sX + (add.count('R') - add.count('L')) * cell_width
        Y = sY + (add.count('D') - add.count('U')) * cell_width
        print(X, Y)
        try:
            if X < (screen_width - cell_width):
                print("1")
                if surface.get_at((X + cell_width, Y))[0:3] !=\
                        (180, 110, 255) and add[-1] != 'L':
                    print("1#", add+'R')
                    path.put(add + 'R')
                    k = 1
                    if surface.get_at((X + cell_width, Y))[0:3] ==\
                            (0, 255, 0):
                        res = add + 'R'
                        print("Found: ", res)
                        break
        except:
            print("1-")
            pass

        try:
            if X > cell_width:
                print("2")
                if surface.get_at((X - cell_width, Y))[0:3] !=\
                        (180, 110, 255) and add[-1] != 'R':
                    print("2#", add + 'L')
                    k = 1
                    path.put(add + 'L')
                    if surface.get_at((X - cell_width, Y))[0:3] ==\
                            (0, 255, 0):
                        res = add + 'L'
                        print("Found: ", res)
                        break

        except:
            print("2-")
            pass
        try:
            if Y > cell_width:
                print("3")
                if surface.get_at((X, Y - cell_width))[0:3] !=\
                        (180, 110, 255) and add[-1] != 'D':
                    print("3#", add + 'U')
                    k = 1
                    path.put(add + 'U')
                    if surface.get_at((X, Y - cell_width))[0:3] ==\
                            (0, 255, 0):
                        res = add + 'U'
                        print("Found: ", res)
                        break
        except:
            print("3-")
            pass
        try:
            if Y < (screen_width - cell_width):
                print("4")
                if surface.get_at((X, Y + cell_width))[0:3] !=\
                        (180, 110, 255) and add[-1] != 'U':
                    print("4#", add + 'D')
                    k = 1
                    path.put(add + 'D')
                    if surface.get_at((X, Y + cell_width))[0:3] ==\
                            (0, 255, 0):
                        res = add + 'D'
                        print("Found: ", res)
                        break
        except:
            print("4-")
            pass

        if k == 0 and path.empty() == True:
            print("Maze not Found")
            Tk().wm_withdraw()
            messagebox.showinfo("Path not found!")
            return

    X = sXX
    Y = sYY

    pygame.draw.rect(surface, (0, 255, 0), ((X, Y), (cell_width, cell_width)))

    for r in res:
        if r == 'L':
            X = X - cell_width
        if r == 'R':
            X = X + cell_width
        if r == 'U':
            Y = Y - cell_width
        if r == 'D':
            Y = Y + cell_width

        pygame.draw.rect(surface, (0, 255, 0), ((X, Y), (cell_width, cell_width)))
    makeMaze(surface, screen_width, cell_num)


def main():

    pygame.init()
    screen_size = 500
    screen_width = 3
    run = True
    lock = 0

    win = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("Breadth First Path Finding Algorithm")
    clock = pygame.time.Clock()
    win.fill((0, 0, 0))
    makeMaze(win, screen_size, screen_width)

    while run:
        clock.tick(10)
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN and lock == 0:
            pos = pygame.mouse.get_pos()
            makeObstacle(win, screen_size, screen_width, pos)
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_SPACE]:
                lock = 1
            if keys[pygame.K_DELETE]:
                randomMatrix(win, screen_size, screen_width)
        if lock == 1:
            Breadth_First_Algorithm(win, screen_size, screen_width)
            lock = 2


main()
