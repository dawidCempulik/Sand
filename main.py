import pygame

import elements
import grid

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand")

FPS = 60
GRID_SIZE = (100, 100)
GRID = grid.Grid(GRID_SIZE)

PIXELS_PER_CELL = (WIDTH / GRID_SIZE[0], HEIGHT / GRID_SIZE[1])


def screen_to_grid(screen_pos: tuple):
    return int(screen_pos[0] / PIXELS_PER_CELL[0]), int(screen_pos[1] / PIXELS_PER_CELL[1])


def draw_grid_lines():
    for x in range(GRID_SIZE[0] - 1):
        posx = WIDTH / GRID_SIZE[0] * (x + 1)
        pygame.draw.line(WIN, (50, 50, 50), (posx, 0), (posx, HEIGHT))
    for y in range(GRID_SIZE[1] - 1):
        posy = HEIGHT / GRID_SIZE[1] * (y + 1)
        pygame.draw.line(WIN, (50, 50, 50), (0, posy), (WIDTH, posy))


def draw_grid():
    #draw_grid_lines()
    GRID.draw_elements(WIN)


def draw_window():
    WIN.fill((0, 0, 0))
    draw_grid()
    pygame.display.update()


def elements_logic():
    GRID.execute_logic()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if pygame.mouse.get_pressed(3)[0]:
            GRID.place(screen_to_grid(pygame.mouse.get_pos()), elements.Sand())
        if pygame.mouse.get_pressed(3)[2]:
            GRID.place(screen_to_grid(pygame.mouse.get_pos()), elements.Stone())

        draw_window()
        elements_logic()
    pygame.quit()


if __name__ == "__main__":
    main()
