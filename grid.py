import pygame
from pygame import Vector2
import elements


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
                pos = Vector2(x, y)
                self.get(pos).draw(surface, pos, self.SIZE)

    def execute_logic(self):
        for x in range(self.SIZE[0]):
            for y in range(self.SIZE[1]):
                pos = Vector2(x, y)
                element = self.get(pos)
                if element.computed:
                    continue
                element.logic(self, pos)

        for x in range(self.SIZE[0]):
            for y in range(self.SIZE[1]):
                pos = Vector2(x, y)
                element = self.get(pos)
                element.computed = False

    def get(self, pos: Vector2) -> elements.Element:
        return self.GRID[int(pos.y)][int(pos.x)]

    def set(self, pos: Vector2, element: elements.Element):
        self.GRID[int(pos.y)][int(pos.x)] = element

    def replace(self, pos1: Vector2, pos2: Vector2):
        temp = self.get(pos2)
        self.set(pos2, self.get(pos1))
        self.set(pos1, temp)

    def place(self, pos: Vector2, element: type) -> bool:
        if isinstance(self.get(pos), elements.Air):
            self.set(pos, element())
            return True
        return False

    def place_line(self, pos1: Vector2, pos2: Vector2, element: type):
        points = []

        dx = abs(pos2.x - pos1.x)
        sx = 1 if pos1.x < pos2.x else -1
        dy = -abs(pos2.y - pos1.y)
        sy = 1 if pos1.y < pos2.y else -1
        error = dx + dy

        while True:
            points.append(pos1.copy())
            if pos1.x == pos2.x and pos1.y == pos2.y:
                break
            e2 = 2 * error
            if e2 >= dy:
                if pos1.x == pos2.x:
                    break
                error = error + dy
                pos1.x = int(pos1.x + sx)

            if e2 <= dx:
                if pos1.y == pos2.y:
                    break
                error = error + dx
                pos1.y = pos1.y + sy

        for point in points:
            self.place(point, element)
