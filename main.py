import pygame

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand")

FPS = 60
GRID_SIZE = (20, 20)


def draw_grid():
    for x in range(GRID_SIZE[0] - 1):
        posx = WIDTH / GRID_SIZE[0] * (x + 1)
        pygame.draw.line(WIN, (255,255,255), (posx, 0), (posx, HEIGHT))
    for y in range(GRID_SIZE[0] - 1):
        posy = HEIGHT / GRID_SIZE[1] * (y + 1)
        pygame.draw.line(WIN, (255,255,255), (0, posy), (WIDTH, posy))


def draw_window():
    draw_grid()
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()