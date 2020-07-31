from Functions import *

draw.board()
while v.running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            mouseX = int(mouseX/100)
            mouseY = int(mouseY/100)
            if mouseX < 8 and mouseY < 8:
                if v.turn == 'red':
                    if v.board[mouseY][mouseX] == 1 or v.board[mouseY][mouseX] == 2:
                        v.selected = [mouseX, mouseY]
                        selected(mouseX, mouseY)
                        checkGame()
                elif v.turn == 'black':
                    if v.board[mouseY][mouseX] == 3 or v.board[mouseY][mouseX] == 4:
                        v.selected = [mouseX, mouseY]
                        selected(mouseX, mouseY)
                        checkGame()