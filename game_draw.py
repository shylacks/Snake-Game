import pygame
import game_snake
# Game settings
HEIGHT, WIDTH = 800, 800
DELAY = 100  # in ms
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
LIGHT_GREEN = (144, 238, 144)


class DrawGame:
    def __init__(self):
        self.game = game_snake.Game()

        # calc size of singe squares
        if len(self.game.board) > len(self.game.board[0]):
            self.w_box = (WIDTH - len(self.game.board) * SPACE) // len(self.game.board)
        else:
            self.w_box = (HEIGHT - len(self.game.board[0]) * SPACE) // len(self.game.board[0])

    def draw_board(self, color):
        # I think there is more elegant way to do it, space for improvement
        x, y = 0, 0
        for row in self.game.board:
            for _ in row:
                box = pygame.Rect(x, y, self.w_box, self.w_box)
                pygame.draw.rect(screen, color, box)
                x = x + self.w_box + SPACE
            y = y + self.w_box + SPACE
            x = 0

    def draw_snake(self, **kwargs):
        head = kwargs.get('head')
        body = kwargs.get('body')
        for el in self.game.body:
            box = pygame.Rect(el[0] * (self.w_box + SPACE), el[1] * (self.w_box + SPACE), self.w_box, self.w_box)
            # pygame.draw.rect(screen, WHITE, box)
            screen.blit(body, box)

        box = pygame.Rect(self.game.position[0] * (self.w_box + SPACE), self.game.position[1] * (self.w_box + SPACE),
                          self.w_box, self.w_box)

        if self.game.direction == "up" or "none":
            screen.blit(head, box)
        if self.game.direction == "left":
            head = pygame.transform.rotate(head, 90)
        if self.game.direction == "down":
            head = pygame.transform.rotate(head, 180)
        if self.game.direction == "right":
            head = pygame.transform.rotate(head, -90)

        screen.blit(head, box)

        # pygame.draw.rect(screen, GREEN, box)

    def draw_fruit(self, fruit):
        box = pygame.Rect(self.game.fruit_position[0] * (self.w_box + SPACE),
                          self.game.fruit_position[1] * (self.w_box + SPACE), self.w_box, self.w_box)

        screen.blit(fruit, box)
        # pygame.draw.rect(screen, RED, box)

    def loop(self):
        while not self.game.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.game_over = True
                # movement keys input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and self.game.direction != "down":
                        self.game.direction = "up"
                    if event.key == pygame.K_s and self.game.direction != "up":
                        self.game.direction = "down"
                    if event.key == pygame.K_a and self.game.direction != "right":
                        self.game.direction = "left"
                    if event.key == pygame.K_d and self.game.direction != "left":
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
            self.draw_board(LIGHT_GREEN)

            apple = pygame.image.load('images/apple.png')
            apple = pygame.transform.scale(apple, (self.w_box, self.w_box))
            self.draw_fruit(apple)

            head = pygame.image.load('images/head.png')
            head = pygame.transform.scale(head, (self.w_box, self.w_box))
            body = pygame.image.load('images/body.png')
            body = pygame.transform.scale(body, (self.w_box, self.w_box))
            self.draw_snake(head=head, body=body)
            pygame.display.flip()
