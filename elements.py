import random

import pygame


class Element:
    COLOR = ()
    computed = False

    def __init__(self, color: tuple):
        self.COLOR = color

    def draw(self, surface: pygame.Surface, pos: tuple, grid_size: tuple):
        pixels_per_cell = (surface.get_width() / grid_size[0], surface.get_height() / grid_size[1])
        rect = pygame.Rect(pixels_per_cell[0] * pos[0], pixels_per_cell[1] * pos[1],
                           pixels_per_cell[0], pixels_per_cell[1])
        pygame.draw.rect(surface, self.COLOR, rect)

    def logic(self, grid, pos: tuple):
        self.computed = True


class Air(Element):
    def __init__(self):
        super().__init__(())

    def draw(self, surface: pygame.Surface, pos: tuple, grid_size: tuple):
        pass


class Sand(Element):
    COLOR = (252, 186, 3)

    def __init__(self):
        super().__init__(self.COLOR)

    def logic(self, grid, pos: tuple):
        super().logic(grid, pos)

        onedown = grid.validate_pos((pos[0], pos[1] + 1))
        if isinstance(grid.get(onedown), Air):
            grid.replace(pos, onedown)
            return

        if random.randint(0, 1) == 0:
            onedownleft = grid.validate_pos((pos[0] - 1, pos[1] + 1))
            if isinstance(grid.get(onedownleft), Air):
                grid.replace(pos, onedownleft)
                return

        onedownright = grid.validate_pos((pos[0] + 1, pos[1] + 1))
        if isinstance(grid.get(onedownright), Air):
            grid.replace(pos, onedownright)
            return

        onedownleft = grid.validate_pos((pos[0] - 1, pos[1] + 1))
        if isinstance(grid.get(onedownleft), Air):
            grid.replace(pos, onedownleft)
            return


class Stone(Element):
    COLOR = (128, 128, 128)

    def __init__(self):
        super().__init__(self.COLOR)

    def logic(self, grid, pos: tuple):
        pass
