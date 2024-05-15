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
                self.get(pos).draw(surface, pos, self.SIZE)

    def execute_logic(self):
        for x in range(self.SIZE[0]):
            for y in range(self.SIZE[1]):
                pos = (x, y)
                element = self.get(pos)
                if element.computed:
                    continue
                element.logic(self, pos)

        for x in range(self.SIZE[0]):
            for y in range(self.SIZE[1]):
                pos = (x, y)
                element = self.get(pos)
                element.computed = False

    def get(self, pos: tuple) -> elements.Element:
        return self.GRID[pos[1]][pos[0]]

    def set(self, pos: tuple, element: elements.Element):
        self.GRID[pos[1]][pos[0]] = element

    def replace(self, current: tuple, new: tuple):
        temp = self.get(new)
        self.set(new, self.get(current))
        self.set(current, temp)

    def place(self, pos: tuple, element: elements.Element) -> bool:
        if isinstance(self.get(pos), elements.Air):
            self.set(pos, element)
            return True
        return False
