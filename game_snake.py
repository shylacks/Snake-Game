import numpy as np
import random

# Globals
HEIGHT, WIDTH = 25, 25
BOARD = HEIGHT, WIDTH
HEAD_COORDINATES = [HEIGHT // 2, WIDTH // 2]


class Game:
    def __init__(self):
        self.board = np.zeros(BOARD)  # init empty board

        # snake
        self.position = HEAD_COORDINATES
        self.previous = []
        self.body = []

        self.direction = "none"
        self.game_over = False
        self.fruit_position = [random.randrange(WIDTH), random.randrange(HEIGHT)]

    def move(self, direction):
        # after first point, append previous position, and trim to the score, so list is always as long as snake
        if self.body:
            self.previous.append([self.position[0], self.position[1]])
            self.previous = self.previous[-len(self.body):]

        if direction == "left":
            self.position[0] -= 1
        if direction == "up":
            self.position[1] -= 1
        if direction == "right":
            self.position[0] += 1
        if direction == "down":
            self.position[1] += 1

        # after move, change position of each snake square
        for i in range(0, len(self.body)):
            self.body[i] = self.previous[i]

    # collision detection with walls and snake himself
    def wall_detection(self):
        if self.position[0] >= WIDTH or self.position[0] < 0 or self.position[1] >= HEIGHT or self.position[1] < 0:
            self.game_over = True

    def snake_hit_self(self):
        if self.position in self.body:
            self.game_over = True

    # check for point, create new fruit,
    def point(self):
        if self.position == self.fruit_position:
            new_fruit_position = [random.randrange(WIDTH), random.randrange(HEIGHT)]
            while new_fruit_position == self.position or new_fruit_position in self.body:
                new_fruit_position = [random.randrange(WIDTH), random.randrange(HEIGHT)]

            # add position to body, then create new fruit
            self.body.append(self.fruit_position)
            self.fruit_position = new_fruit_position
