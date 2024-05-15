import pygame
import elements
from typing import Self


class Grid:
    SIZE = ()
    GRID = []

    def __init__(self, size: tuple):
        self.SIZE = size

        for y in range(size[1]):
            self.GRID.append([])
            for x in range(size[0]):
                self.GRID[y].append(elements.Air())

    def draw_elements(self, surface: pygame.Surface):
        for x in range(self.SIZE[0]):
            for y in range(self.SIZE[1]):
                pos = (x, y)
                self.get(pos).draw(surface, pos)

    def execute_logic(self):
        for x in range(self.SIZE[0]):
            for y in range(self.SIZE[1]):
                pos = (x, y)
                self.get(pos).logic(self, pos)

    def get(self, pos: tuple) -> elements.Element:
        return self.GRID[-pos[1] - 1][pos[0]]

    def set(self, pos: tuple, element: elements.Element):
        self.GRID[-pos[1] - 1][pos[0]] = element

    def replace(self, pos1: tuple, pos2: tuple):
        temp = self.get(pos2)
        self.set(pos2, self.get(pos1))

    def chunk(self, pos: tuple, size: tuple) -> Self:
        grid = Grid(size)
        for i in range(size[0]):
            for j in range(size[1]):
                grid.set((i, j), self.get((pos[0] + i, pos[1] + j)))

        return grid
