import pygame
import game_snake
# Game settings
HEIGHT, WIDTH = 800, 800
DELAY = 60  # in ms
SPACE = 0  # space between squares

# Pygame settings
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (30, 28, 28)
BLACK = (0, 0, 0)


class DrawGame:
    def __init__(self):
        self.game = game_snake.Game()

        # calc size of singe squares
        if len(self.game.board) > len(self.game.board[0]):
            self.w_box = (WIDTH - len(self.game.board) * SPACE) // len(self.game.board)
        else:
            self.w_box = (HEIGHT - len(self.game.board[0]) * SPACE) // len(self.game.board[0])

    def draw_board(self):
        # I think there is more elegant way to do it, space for improvement
        x, y = 0, 0
        for row in self.game.board:
            for _ in row:
                box = pygame.Rect(x, y, self.w_box, self.w_box)
                pygame.draw.rect(screen, BLACK, box)
                x = x + self.w_box + SPACE
            y = y + self.w_box + SPACE
            x = 0

    def draw_snake(self):
        #  first draw head then body for better animation

        for el in self.game.body:
            box = pygame.Rect(el[0] * (self.w_box + SPACE), el[1] * (self.w_box + SPACE), self.w_box, self.w_box)
            pygame.draw.rect(screen, WHITE, box)

        box = pygame.Rect(self.game.position[0] * (self.w_box + SPACE), self.game.position[1] * (self.w_box + SPACE),
                          self.w_box, self.w_box)
        pygame.draw.rect(screen, GREEN, box)

    def draw_fruit(self):
        box = pygame.Rect(self.game.fruit_position[0] * (self.w_box + SPACE),
                          self.game.fruit_position[1] * (self.w_box + SPACE), self.w_box, self.w_box)
        pygame.draw.rect(screen, RED, box)

    def loop(self):
        while not self.game.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.game_over = True
                # movement keys input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.game.direction = "up"
                    if event.key == pygame.K_s:
                        self.game.direction = "down"
                    if event.key == pygame.K_a:
                        self.game.direction = "left"
                    if event.key == pygame.K_d:
                        self.game.direction = "right"

            # move is one key is pressed
            pygame.time.delay(DELAY)
            self.game.move(self.game.direction)

            # check collisions
            self.game.wall_detection()
            self.game.snake_hit_self()

            # if not check is there a point
            self.game.point()

            # DRAW
            self.draw_board()
            self.draw_fruit()
            self.draw_snake()
            pygame.display.flip()
