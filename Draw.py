import Variables as v
import pygame

pygame.init()


def token(x, y):
    if v.board[x][y] == 1:
        v.screen.blit(v.redTok, ((y * 100) + 10, (x * 100) + 10))
    elif v.board[x][y] == 2:
        v.screen.blit(v.redkingTok, ((y * 100) + 10, (x * 100) + 10))
    elif v.board[x][y] == 3:
        v.screen.blit(v.blackTok, ((y * 100) + 10, (x * 100) + 10))
    elif v.board[x][y] == 4:
        v.screen.blit(v.blackkingTok, ((y * 100) + 10, (x * 100) + 10))


def board():
    if v.board[0][0] == 3:
        v.board[0][0] = 4
    if v.board[0][2] == 3:
        v.board[0][2] = 4
    if v.board[0][4] == 3:
        v.board[0][4] = 4
    if v.board[0][6] == 3:
        v.board[0][6] = 4
    if v.board[7][1] == 1:
        v.board[7][1] = 2
    if v.board[7][3] == 1:
        v.board[7][3] = 2
    if v.board[7][5] == 1:
        v.board[7][5] = 2
    if v.board[7][7] == 1:
        v.board[7][7] = 2

    v.screen.fill(v.black)
    pygame.draw.rect(v.screen, v.red, (0, 0, 100, 100))
    pygame.draw.rect(v.screen, v.red, (200, 0, 100, 100))
    pygame.draw.rect(v.screen, v.red, (400, 0, 100, 100))
    pygame.draw.rect(v.screen, v.red, (600, 0, 100, 100))
    pygame.draw.rect(v.screen, v.red, (100, 100, 100, 100))
    pygame.draw.rect(v.screen, v.red, (300, 100, 100, 100))
    pygame.draw.rect(v.screen, v.red, (500, 100, 100, 100))
    pygame.draw.rect(v.screen, v.red, (700, 100, 100, 100))
    pygame.draw.rect(v.screen, v.red, (0, 200, 100, 100))
    pygame.draw.rect(v.screen, v.red, (200, 200, 100, 100))
    pygame.draw.rect(v.screen, v.red, (400, 200, 100, 100))
    pygame.draw.rect(v.screen, v.red, (600, 200, 100, 100))
    pygame.draw.rect(v.screen, v.red, (100, 300, 100, 100))
    pygame.draw.rect(v.screen, v.red, (300, 300, 100, 100))
    pygame.draw.rect(v.screen, v.red, (500, 300, 100, 100))
    pygame.draw.rect(v.screen, v.red, (700, 300, 100, 100))
    pygame.draw.rect(v.screen, v.red, (0, 400, 100, 100))
    pygame.draw.rect(v.screen, v.red, (200, 400, 100, 100))
    pygame.draw.rect(v.screen, v.red, (400, 400, 100, 100))
    pygame.draw.rect(v.screen, v.red, (600, 400, 100, 100))
    pygame.draw.rect(v.screen, v.red, (100, 500, 100, 100))
    pygame.draw.rect(v.screen, v.red, (300, 500, 100, 100))
    pygame.draw.rect(v.screen, v.red, (500, 500, 100, 100))
    pygame.draw.rect(v.screen, v.red, (700, 500, 100, 100))
    pygame.draw.rect(v.screen, v.red, (0, 600, 100, 100))
    pygame.draw.rect(v.screen, v.red, (200, 600, 100, 100))
    pygame.draw.rect(v.screen, v.red, (400, 600, 100, 100))
    pygame.draw.rect(v.screen, v.red, (600, 600, 100, 100))
    pygame.draw.rect(v.screen, v.red, (100, 700, 100, 100))
    pygame.draw.rect(v.screen, v.red, (300, 700, 100, 100))
    pygame.draw.rect(v.screen, v.red, (500, 700, 100, 100))
    pygame.draw.rect(v.screen, v.red, (700, 700, 100, 100))

    for x in range(8):
        for y in range(8):
            token(x, y)

    if v.turn == 'red':
        pygame.draw.circle(v.screen, v.blue, (825, 350), 15)
    elif v.turn == 'black':
        pygame.draw.circle(v.screen, v.blue, (825, 450), 15)
    pygame.draw.line(v.screen, v.red, (800, 0), (800, 800), 1)