import pygame
import random

class Rectangulo:
    def __init__(self, window):
        self.window = window
        self.width = random.randint(20, 100)
        self.height = random.randint(20, 100)
        self.x = random.randint(0, window.get_width() - self.width)
        self.y = random.randint(0, window.get_height() - self.height)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))

    def clickedInside(self, pos):
        return self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height

    def __eq__(self, other):
        return self.width * self.height == other.width * other.height

    def __lt__(self, other):
        return self.width * self.height < other.width * other.height

    def __le__(self, other):
        return self.width * self.height <= other.width * other.height

    def __gt__(self, other):
        return self.width * self.height > other.width * self.height

    def __ge__(self, other):
        return self.width * self.height >= other.width * other.height
