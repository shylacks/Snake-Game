import pygame
import game_snake

# Game settings
WIDTH = 700
DELAY = 123  # in ms
SPACE = 1  # space between squares

# Pygame settings
pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Snake")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class DrawGame:
    def __init__(self):
        self.game = game_snake.Game()
        self.w_box = ((WIDTH - SPACE*len(self.game.board)) // len(self.game.board))  # calc size of singe square

    # func to draw anything, in the future
    def draw(self, something):
        pass

    def draw_board(self):
        # I think there is more elegant way to do it, space for improvement
        x, y = 0, 0
        for row in self.game.board:
            for _ in row:
                box = pygame.Rect(x, y, self.w_box, self.w_box)
                pygame.draw.rect(screen, WHITE, box)
                x = x + self.w_box + SPACE
            y = y + self.w_box + SPACE
            x = 0

    def draw_snake(self):
        #  first draw head then body for better animation
        for el in self.game.body:
            box = pygame.Rect(el[0] * (self.w_box + SPACE), el[1] * (self.w_box + SPACE), self.w_box, self.w_box)
            pygame.draw.rect(screen, RED, box)
        box = pygame.Rect(self.game.position[0]*(self.w_box+SPACE), self.game.position[1]*(self.w_box+SPACE), self.w_box, self.w_box)
        pygame.draw.rect(screen, (0, 0, 0), box)

    def draw_fruit(self):
        box = pygame.Rect(self.game.fruit_position[0] * (self.w_box + SPACE), self.game.fruit_position[1] * (self.w_box + SPACE), self.w_box, self.w_box)
        pygame.draw.rect(screen, GREEN, box)

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
            # if not check if there is point
            self.game.point()

            # DRAW
            self.draw_board()
            self.draw_fruit()
            self.draw_snake()
            pygame.display.flip()
