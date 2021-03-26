#Sudoku solver using backtracking
#Github: https://github.com/maxikichka/sudoku-solver-with-backtracking

#Helpful resources:

#https://www.youtube.com/watch?v=eqUwSA0xI-s&t=2s

#https://www.geeksforgeeks.org/backtracking-algorithms/

#https://en.wikipedia.org/wiki/Backtracking

#https://www.tutorialspoint.com/introduction-to-backtracking-algorithms


board = [[0, 3, 2, 0, 0, 5, 9, 0, 0], [6, 8, 0, 0, 0, 0, 4, 7, 0], [4, 9, 0, 0, 7, 0, 3, 1, 2], [2, 5, 0, 0, 9, 7, 8, 3, 0], [0, 0, 6, 3, 5, 0, 7, 0, 0], [0, 0, 3, 1, 2, 0, 6, 5, 4], [0, 4, 9, 0, 6, 1, 0, 0, 0], [5, 0, 0, 0, 4, 3, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 4, 0]]


import os
import time
import pygame
from tkinter import *


pygame.init()
pygame.font.init()

font = pygame.font.SysFont(None, 70)

WIDTH = 630
HEIGHT = 730

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku Solver By Max Trushkov')

squareSize = WIDTH//9

def buildBoard():
    global start

    
    for i in range(len(pixels)):
        for j in range(len(pixels[i])):
            board[i][j] = int(pixels[i][j].get())

    root.destroy()

    start = time.time()

    solve()

        
    


def askUserForBoard():
    global pixels, root

    pixels = []
    
    root = Tk()

    root.title("Make Board")

    

    for i in range(9):
        pixels.append([])
        for j in range(9):
            pixel = Entry(width=3)
            pixel.insert(INSERT, str(board[i][j]))
            pixel.grid(row=i, column=j)
            pixels[-1].append(pixel)

    submit = Button(root, text="Solve", command = buildBoard)
    
    submit.grid(row=0, column=9)

    root.mainloop()


def done():
    end = time.time()


    main = True

    while main:
        win.fill((255, 255, 255))

        y = 0

        for i in range(len(board)):
            x = 0
            for j in range(len(board[i])):

                text = font.render(str(board[i][j]), True, (0, 0, 0))

                pygame.draw.rect(win, (0, 0, 0), (x, y, squareSize, squareSize), 2)
                win.blit(text, (x + 10, y + 10))
                x += squareSize
            y += squareSize


        pygame.draw.line(win, (0, 0, 0), (WIDTH//3, 0), (WIDTH//3, HEIGHT - 100), 7)

        pygame.draw.line(win, (0, 0, 0), (WIDTH//3 * 2, 0), (WIDTH//3 * 2, HEIGHT - 100), 7)

        pygame.draw.line(win, (0, 0, 0), (0, (HEIGHT- 100)//3), (WIDTH, (HEIGHT-100)//3), 7)

        pygame.draw.line(win, (0, 0, 0), (0, (HEIGHT-100)//3*2), (WIDTH, (HEIGHT-100)//3*2), 7)

            

        text = font.render("Finished in : " + str(end-start), True, (0, 0, 0))

        win.blit(text, (10, HEIGHT-100))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False

        pygame.display.update()
    pygame.quit()


def solve():
    
    value = findEmptyPoses()

    if not value:
        done()
        return True
    else:
        row = value[0]
        col = value[1]

    win.fill((255, 255, 255))

    
    draw_board(value)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main = False

    for numG in range(board[row][col] + 1, 10):
        if isValid(numG, row, col):
            board[row][col] = numG

            if solve():
                done()
                return True

            board[row][col] = 0
    pygame.display.update()


    return False


def isValid(numG, row, col):

    if numG in board[row]:

        return False

    for i in range(len(board)):
        if board[i][col] == numG and i != row:
            return False


        startX = (row) - ((row) % 3)
        startY = (col) - ((col) % 3)

        for x in range(startX, startX + 3):
            for m in range(startY, startY + 3):
                if board[x][m] == numG:
                    return False




    return True

def findEmptyPoses():

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return [i, j]

    return False


def draw_board(value):

    y = 0

    for i in range(len(board)):
        x = 0
        for j in range(len(board[i])):
            if [i, j] == value:
                text = font.render(str(board[i][j]), True, (0, 255, 0))
            else:
                text = font.render(str(board[i][j]), True, (0, 0, 0))

            pygame.draw.rect(win, (0, 0, 0), (x, y, squareSize, squareSize), 2)
            win.blit(text, (x + 10, y + 10))
            x += squareSize
        y += squareSize

    pygame.draw.line(win, (0, 0, 0), (WIDTH//3, 0), (WIDTH//3, HEIGHT - 100), 7)

    pygame.draw.line(win, (0, 0, 0), (WIDTH//3 * 2, 0), (WIDTH//3 * 2, HEIGHT - 100), 7)

    pygame.draw.line(win, (0, 0, 0), (0, (HEIGHT-100)//3), (WIDTH, (HEIGHT - 100)//3), 7)

    pygame.draw.line(win, (0, 0, 0), (0, (HEIGHT-100)//3*2), (WIDTH, (HEIGHT-100)//3*2), 7)

    
askUserForBoard()
