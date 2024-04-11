import random

import pygame

pygame.init()

class Game:
    def __init__(self):
        self.ROWS = 4
        self.COLUMNS = 4
        self.TILE_SIZE = 200
        self.border = 4

        self.colors = {0 : (204,192,179), 2 : (238,228,218), 4 : (236,224,200), 8 : (242,177,121), 16 : (245,149,99), 32: (245,124,95), 64 : (246,93,59), 128 : (237,206,113), 256 : (237,204,97), 512 : (236,200,80), 1024 : (237,197,63), 2048 : (63,57,50)}

        self.board = [[0 for _ in range(self.COLUMNS)] for i in range(self.ROWS)]
        self.empty_tiles = [(x, y) for x in range(self.COLUMNS) for y in range(self.ROWS)]

        self.width = self.COLUMNS * self.TILE_SIZE
        self.height = self.ROWS * self.TILE_SIZE

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.running = True
        self.gameOver = False
        self.add_number(2)

    def resetGame(self):
        self.board = [[0 for _ in range(self.COLUMNS)] for i in range(self.ROWS)]
        self.empty_tiles = [(x, y) for x in range(self.COLUMNS) for y in range(self.ROWS)]
        self.add_number(2)
        self.gameOver = False

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if self.gameOver:
                    self.resetGame()
                moved = False
                if event.key == pygame.K_LEFT:
                    moved = True
                    i = 0
                    merged = False
                    while i < self.COLUMNS and merged is False:
                        i += 1
                        for r in range(self.ROWS):
                            # has_square = False
                            # zero_encountered = False
                            # for i in self.board[r]:
                            #     if i == 0:
                            #         zero_encountered = True
                            #     if i != 0 and zero_encountered:
                            #         has_square = True
                            #         break
                            # # if self.board[r][0] == 0 and has_square:
                            # #     empty_spaces = True
                            for c in range(1, self.COLUMNS):
                                if self.board[r][c] != 0 and (self.board[r][c - 1] == 0 or self.board[r][c - 1] == self.board[r][c]):
                                    if self.board[r][c-1] == self.board[r][c] and self.board[r][c] != 0:
                                        self.board[r][c-1] = self.board[r][c] + self.board[r][c - 1]
                                        self.empty_tiles.append((c, r))
                                        merged = True
                                    else:
                                        self.board[r][c - 1] = self.board[r][c]
                                        self.empty_tiles.remove((c - 1, r))
                                        self.empty_tiles.append((c, r))
                                    self.board[r][c] = 0
                if event.key == pygame.K_RIGHT:
                    moved = True
                    i = 0
                    merged = False
                    while i < self.COLUMNS and merged is False:
                        i += 1
                        for r in range(self.ROWS):
                            for c1 in range(0, self.COLUMNS - 1):
                                c = self.COLUMNS - 2 - c1
                                if self.board[r][c] != 0 and (self.board[r][c + 1] == 0 or self.board[r][c + 1] == self.board[r][c]):
                                    if self.board[r][c+1] == self.board[r][c] and self.board[r][c] != 0:
                                        self.board[r][c+1] = self.board[r][c] + self.board[r][c + 1]
                                        self.empty_tiles.append((c, r))
                                        merged = True
                                    else:
                                        self.board[r][c + 1] = self.board[r][c]
                                        self.empty_tiles.remove((c + 1, r))
                                        self.empty_tiles.append((c, r))
                                    self.board[r][c] = 0
                if event.key == pygame.K_UP:
                    moved = True
                    i = 0
                    merged = False
                    while i < self.ROWS and merged is False:
                        i += 1
                        for c in range(self.COLUMNS):
                            for r in range(1, self.ROWS):
                                if self.board[r][c] != 0 and (self.board[r - 1][c] == 0 or self.board[r - 1][c] == self.board[r][c]):
                                    if self.board[r - 1][c] == self.board[r][c] and self.board[r][c] != 0:
                                        self.board[r - 1][c] = self.board[r][c] + self.board[r - 1][c]
                                        self.empty_tiles.append((c, r))
                                        merged = True
                                    else:
                                        self.board[r - 1][c] = self.board[r][c]
                                        self.empty_tiles.remove((c, r - 1))
                                        self.empty_tiles.append((c, r))
                                    self.board[r][c] = 0
                if event.key == pygame.K_DOWN:
                    moved = True
                    i = 0
                    merged = False
                    while i < self.ROWS and merged is False:
                        i += 1
                        for c in range(self.COLUMNS):
                            for r1 in range(0, self.ROWS - 1):
                                r = self.COLUMNS - 2 - r1
                                if self.board[r][c] != 0 and (self.board[r + 1][c] == 0 or self.board[r + 1][c] == self.board[r][c]):
                                    if self.board[r + 1][c] == self.board[r][c] and self.board[r][c] != 0:
                                        self.board[r + 1][c] = self.board[r][c] + self.board[r + 1][c]
                                        self.empty_tiles.append((c, r))
                                        merged = True
                                    else:
                                        self.board[r + 1][c] = self.board[r][c]
                                        self.empty_tiles.remove((c, r + 1))
                                        self.empty_tiles.append((c, r))
                                    self.board[r][c] = 0
                if moved:
                    if random.randint(0, 100) < 10:
                        self.add_number(4)
                    else:
                        self.add_number(2)

        for r, row_val in enumerate(self.board):
            for c, column_val in enumerate(row_val):
                rect = pygame.Rect(c * self.TILE_SIZE, r * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)

                pygame.draw.rect(self.screen, self.colors[column_val], rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, self.border)
                if column_val != 0:
                    font = pygame.font.SysFont('Comic Sans MS', self.TILE_SIZE // 4)
                    text = font.render(str(column_val), True, (0, 0, 0))
                    textRect = text.get_rect()
                    textRect.center = rect.center
                    self.screen.blit(text, textRect)

        if self.gameOver:
            font = pygame.font.SysFont('Comic Sans MS', self.TILE_SIZE // 2)
            text = font.render("GAME OVER", True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (self.width // 2, self.height // 2)
            self.screen.blit(text, textRect)


        pygame.display.update()

    def add_number(self, number):
        if len(self.empty_tiles) > 0:
            c, r = random.choice(self.empty_tiles)
            self.board[r][c] = number
            self.empty_tiles.remove((c, r))
        else:
            canMove = False
            for r in range(0, self.ROWS):
                for c in range(self.COLUMNS):
                    current_square = self.board[r][c]
                    try:
                        if c > 0 and self.board[r][c - 1] == current_square:
                            canMove = True
                        if self.board[r][c + 1] == current_square:
                            canMove = True
                        if self.board[r + 1][c] == current_square:
                            canMove = True
                        if r > 0 and self.board[r - 1][c] == current_square:
                            canMove = True
                    except:
                        pass
            if canMove == False:
                self.gameOver = True
                print("GAME OVER")

game = Game()
while game.running:
    game.render()