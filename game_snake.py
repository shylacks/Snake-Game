import numpy as np
import random

# Globals
X = 10
BOARD = X, X
HEAD_POS = [X//2, X//2]


class Game:
    def __init__(self):
        self.board = np.zeros(BOARD)

        # snake
        self.position = HEAD_POS
        self.previous = []
        self.body = []

        self.direction = "none"
        self.game_over = False
        self.fruit_position = [random.randrange(X), random.randrange(X)]

    def move(self, direction):
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

        for i in range(0, len(self.body)):
            if i == 0:
                self.body[0] = self.previous[0]
            if i >= 1:
                self.body[i] = self.previous[i]

    # collision detection with walls and snake himself
    def wall_detection(self):
        if self.position[0] >= X or self.position[0] < 0 or self.position[1] >= X or self.position[1] < 0:
            self.game_over = True

    def snake_hit_self(self):
        if self.position in self.body:
            self.game_over = True

    # check for point, create new fruit,
    def point(self):
        if self.position == self.fruit_position:

            new_fruit_position = [random.randrange(X), random.randrange(X)]
            while new_fruit_position == self.position or new_fruit_position in self.body:
                new_fruit_position = [random.randrange(X), random.randrange(X)]

            # add position to body, then create new fruit
            self.body.append(self.fruit_position)
            self.fruit_position = new_fruit_position
