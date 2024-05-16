import pygame
from pygame import Vector2
import elements
import grid

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand")

clock = pygame.time.Clock()
FPS = 60
GRID_SIZE = (100, 100)
GRID = grid.Grid(GRID_SIZE)

PIXELS_PER_CELL = (WIDTH / GRID_SIZE[0], HEIGHT / GRID_SIZE[1])


def screen_to_grid(screen_pos: tuple):
    grid_pos = Vector2(int(screen_pos[0] / PIXELS_PER_CELL[0]), int(screen_pos[1] / PIXELS_PER_CELL[1]))
    if grid_pos.x < 0 or grid_pos.y < 0 or grid_pos.x >= GRID_SIZE[0] or grid_pos.y >= GRID_SIZE[1]:
        return None
    return grid_pos


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


pygame.font.init()
font = pygame.font.SysFont("Arial", 18, bold=True)


def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    WIN.blit(fps_t, (0, 0))


def draw_window():
    WIN.fill((0, 0, 0))
    fps_counter()
    draw_grid()
    pygame.display.update()


def elements_logic():
    GRID.execute_logic()


def main():
    run = True

    current_element = elements.Sand

    last_mouse_pos = ()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    current_element = elements.Sand
                if event.key == pygame.K_2:
                    current_element = elements.Stone

        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed(3)[0]:
            grid_pos = screen_to_grid(mouse_pos)
            grid_old_pos = screen_to_grid(last_mouse_pos)
            if grid_pos is not None and grid_old_pos is not None:
                GRID.place_line(grid_old_pos, grid_pos, current_element)
        last_mouse_pos = mouse_pos

        draw_window()
        elements_logic()
    pygame.quit()


if __name__ == "__main__":
    main()
