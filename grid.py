import elements
from typing import Self


class Grid:
    SIZE = ()
    GRID = []

    def __init__(self, size: tuple):
        self.SIZE = size

        for y in range(size[0]):
            self.GRID.append([])
            for x in range(size[1]):
                self.GRID[y].append([elements.Air()])

    def get(self, pos: tuple) -> elements.Element:
        return self.GRID[pos[1]][pos[0]]

    def set(self, pos: tuple, element: elements.Element):
        self.GRID[pos[1]][pos[0]] = element

    def chunk(self, pos: tuple, size: tuple) -> Self:
        grid = Grid(size)
        for i in range(size[0]):
            for j in range(size[1]):
                grid.set((i, j), self.get((pos[0] + i, pos[1] + j)))

        return grid
