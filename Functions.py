import pygame
import Variables as v
import Draw as draw

pygame.init()

def turn():
    if v.turn == 'red':
        v.turn = 'black'
    elif v.turn == 'black':
        v.turn = 'red'

def ul(x, y):
    if x - 1 >= 0 and y - 1 >= 0:
        if v.board[y - 1][x - 1] == 0:
            v.moves.append(x - 1)
            v.moves.append(y - 1)
        elif v.turn == 'red':
            if v.board[y - 1][x - 1] == 3 or v.board[y - 1][x - 1] == 4:
                if x - 2 >= 0 and y - 2 >= 0:
                    if v.board[y - 2][x - 2] == 0:
                        v.moves.append(x - 2)
                        v.moves.append(y - 2)
        elif v.turn == 'black':
            if v.board[y - 1][x - 1] == 1 or v.board[y - 1][x - 1] == 2:
                if x - 2 >= 0 and y - 2 >= 0:
                    if v.board[y - 2][x - 2] == 0:
                        v.moves.append(x - 2)
                        v.moves.append(y - 2)


def ur(x, y):
    if x + 1 < 8 and y - 1 >= 0:
        if v.board[y - 1][x + 1] == 0:
            v.moves.append(x + 1)
            v.moves.append(y - 1)
        elif v.turn == 'red':
            if v.board[y - 1][x + 1] == 3 or v.board[y - 1][x + 1] == 4:
                if x + 2 < 8 and y - 2 >= 0:
                    if v.board[y - 2][x + 2] == 0:
                        v.moves.append(x + 2)
                        v.moves.append(y - 2)
        elif v.turn == 'black':
            if v.board[y - 1][x + 1] == 1 or v.board[y - 1][x + 1] == 2:
                if x + 2 < 8 and y - 2 >= 0:
                    if v.board[y - 2][x + 2] == 0:
                        v.moves.append(x + 2)
                        v.moves.append(y - 2)


def dl(x, y):
    if x - 1 >= 0 and y + 1 < 8:
        if v.board[y + 1][x - 1] == 0:
            v.moves.append(x - 1)
            v.moves.append(y + 1)
        elif v.turn == 'red':
            if v.board[y + 1][x - 1] == 3 or v.board[y + 1][x - 1] == 4:
                if x - 2 >= 0 and y + 2 < 8:
                    if v.board[y + 2][x - 2] == 0:
                        v.moves.append(x - 2)
                        v.moves.append(y + 2)
        elif v.turn == 'black':
            if v.board[y + 1][x - 1] == 1 or v.board[y + 1][x - 1] == 2:
                if x - 2 >= 0 and y + 2 < 8:
                    if v.board[y + 2][x - 2] == 0:
                        v.moves.append(x - 2)
                        v.moves.append(y + 2)


def dr(x, y):
    if x + 1 < 8 and y + 1 < 8:
        if v.board[y + 1][x + 1] == 0:
            v.moves.append(x + 1)
            v.moves.append(y + 1)
        elif v.turn == 'red':
            if v.board[y + 1][x + 1] == 3 or v.board[y + 1][x + 1] == 4:
                if x + 2 < 8 and y + 2 < 8:
                    if v.board[y + 2][x + 2] == 0:
                        v.moves.append(x + 2)
                        v.moves.append(y + 2)
        elif v.turn == 'black':
            if v.board[y + 1][x + 1] == 1 or v.board[y + 1][x + 1] == 2:
                if x + 2 < 8 and y + 2 < 8:
                    if v.board[y + 2][x + 2] == 0:
                        v.moves.append(x + 2)
                        v.moves.append(y + 2)

def kill(move):
    killX = int((v.moves[move] - v.selected[0]) / 2 + v.selected[0])
    killY = int((v.moves[move + 1] - v.selected[1]) / 2 + v.selected[1])
    v.board[killY][killX] = 0

def selected(x, y):
    pygame.draw.circle(v.screen, v.blue, (x * 100 + 50, y * 100 + 50), 40, 10)
    v.moves = []
    if v.board[y][x] == 1:
        dl(x, y)
        dr(x, y)
    elif v.board[y][x] == 2:
        ul(x, y)
        ur(x, y)
        dl(x, y)
        dr(x, y)
    elif v.board[y][x] == 3:
        ul(x, y)
        ur(x, y)
    elif v.board[y][x] == 4:
        ul(x, y)
        ur(x, y)
        dl(x, y)
        dr(x, y)
    if len(v.moves) > 0:
        pygame.draw.rect(v.screen, v.blue, (v.moves[0] * 100, v.moves[1] * 100, 100, 100))
        if len(v.moves) > 2:
            pygame.draw.rect(v.screen, v.blue, (v.moves[2] * 100, v.moves[3] * 100, 100, 100))
        if len(v.moves) > 4:
            pygame.draw.rect(v.screen, v.blue, (v.moves[4] * 100, v.moves[5] * 100, 100, 100))
        if len(v.moves) > 6:
            pygame.draw.rect(v.screen, v.blue, (v.moves[6] * 100, v.moves[7] * 100, 100, 100))
    while v.running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                v.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                mouseX = int(mouseX / 100)
                mouseY = int(mouseY / 100)
                if mouseX < 8 and mouseY < 8:
                    if v.selected[0] == mouseX and v.selected[1] == mouseY:
                        v.selected = []
                        draw.board()
                        return
                    if len(v.moves) > 0:
                        if v.moves[0] == mouseX and v.moves[1] == mouseY:
                            v.board[mouseY][mouseX] = v.board[v.selected[1]][v.selected[0]]
                            v.board[v.selected[1]][v.selected[0]] = 0
                            if abs(v.moves[0] - v.selected[0]) != 1:
                                kill(0)
                            else:
                                turn()
                            v.selected = []
                            draw.board()
                            return
                        if len(v.moves) > 2:
                            if v.moves[2] == mouseX and v.moves[3] == mouseY:
                                v.board[mouseY][mouseX] = v.board[v.selected[1]][v.selected[0]]
                                v.board[v.selected[1]][v.selected[0]] = 0
                                if abs(v.moves[2] - v.selected[0]) != 1:
                                    kill(2)
                                else:
                                    turn()
                                v.selected = []
                                draw.board()
                                return
                        if len(v.moves) > 4:
                            if v.moves[4] == mouseX and v.moves[5] == mouseY:
                                v.board[mouseY][mouseX] = v.board[v.selected[1]][v.selected[0]]
                                v.board[v.selected[1]][v.selected[0]] = 0
                                if abs(v.moves[4] - v.selected[0]) != 1:
                                    kill(4)
                                else:
                                    turn()
                                v.selected = []
                                draw.board()
                                return
                        if len(v.moves) > 6:
                            if v.moves[6] == mouseX and v.moves[7] == mouseY:
                                v.board[mouseY][mouseX] = v.board[v.selected[1]][v.selected[0]]
                                v.board[v.selected[1]][v.selected[0]] = 0
                                if abs(v.moves[6] - v.selected[0]) != 1:
                                    kill(6)
                                else:
                                    turn()
                                v.selected = []
                                draw.board()
                                return

def game(player):
    if player == 'red':
        v.screen.fill(v.red)
    elif player == 'black':
        v.screen.fill(v.black)

def checkGame():
    if (not any(1 in x for x in v.board)) and (not any(2 in x for x in v.board)):
        game('black')
    elif (not any(3 in x for x in v.board)) and (not any(4 in x for x in v.board)):
        game('red')