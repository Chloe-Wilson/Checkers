import pygame

pygame.init()

red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((850, 800))

board = [[1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 3, 0, 3, 0, 3, 0, 3], [3, 0, 3, 0, 3, 0, 3, 0], [0, 3, 0, 3, 0, 3, 0, 3]]

redTok = pygame.image.load('red.png')
redTok = pygame.transform.scale(redTok, (80, 80))
blackTok = pygame.image.load('black.png')
blackTok = pygame.transform.scale(blackTok, (80, 80))
redkingTok = pygame.image.load('redking.png')
redkingTok = pygame.transform.scale(redkingTok, (80, 80))
blackkingTok = pygame.image.load('blackking.png')
blackkingTok = pygame.transform.scale(blackkingTok, (80, 80))

running = True
turn = 'red'
selected = []
moves = []