import pygame


class Element:
    COLOR = ()
    GRID_SIZE = ()

    def __init__(self, grid_size: tuple, color: tuple):
        self.GRID_SIZE = grid_size
        self.COLOR = color

    def draw(self, surface: pygame.Surface, pos: tuple):
        rect = pygame.Rect(surface.get_width() / self.GRID_SIZE[0] * pos[0],
                           surface.get_height() / self.GRID_SIZE[1] * pos[1])
        pygame.draw.rect(surface, self.COLOR, rect)

    def logic(self, grid, pos: tuple):
        pass


class Air(Element):
    def __init__(self):
        super().__init__((), ())

    def draw(self, surface: pygame.Surface, pos: tuple):
        pass


class Sand(Element):
    COLOR = (252, 186, 3)

    def __init__(self, grid_size: tuple):
        super().__init__(grid_size, self.COLOR)

    def logic(self, grid, pos: tuple):
        if isinstance(grid.get((pos[0], pos[1] - 1)), Air):
            grid.replace(pos, (pos[0], pos[1] - 1))
