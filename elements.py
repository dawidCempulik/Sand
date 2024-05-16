import random
import math
import pygame
from pygame.math import Vector2


class Element:
    COLOR = ()
    computed = False

    def __init__(self, color: tuple):
        self.COLOR = color

    def draw(self, surface: pygame.Surface, pos: Vector2, grid_size: tuple):
        pixels_per_cell = (surface.get_width() / grid_size[0], surface.get_height() / grid_size[1])
        rect = pygame.Rect(pixels_per_cell[0] * pos.x, pixels_per_cell[1] * pos.y,
                           pixels_per_cell[0], pixels_per_cell[1])
        pygame.draw.rect(surface, self.COLOR, rect)

    def logic(self, grid, pos: Vector2):
        self.computed = True


class Air(Element):
    def __init__(self):
        super().__init__(())

    def draw(self, surface: pygame.Surface, pos: Vector2, grid_size: tuple):
        pass


class Solid(Element):
    pass


class MovableSolid(Solid):
    def logic(self, grid, pos: Vector2):
        super().logic(grid, pos)

        newy = pos.y + 1
        newx = pos.x
        if newy >= grid.SIZE[1]:
            return

        newpos = Vector2(newx, newy)
        if isinstance(grid.get(newpos), Air):
            grid.replace(pos, newpos)
            return

        leftfree, rightfree = False, False

        if pos.x != 0:
            temp = Vector2(pos.x - 1, newy)
            if isinstance(grid.get(temp), Air):
                newpos = Vector2(pos.x - 1, newy)
                leftfree = True

        if pos[0] != grid.SIZE[0] - 1:
            temp = Vector2(pos[0] + 1, newy)
            if isinstance(grid.get(temp), Air):
                newpos = Vector2(pos[0] + 1, newy)
                rightfree = True

        if (not leftfree) and (not rightfree):
            return

        if leftfree and rightfree:
            if random.randint(0, 1) == 0:
                newpos = Vector2(pos[0] - 1, newy)
            else:
                newpos = Vector2(pos[0] + 1, newy)

        grid.replace(pos, newpos)

        
class Sand(MovableSolid):
    COLOR = (252, 186, 3)

    def __init__(self):
        super().__init__(self.COLOR)


class Stone(Solid):
    COLOR = (128, 128, 128)

    def __init__(self):
        super().__init__(self.COLOR)
