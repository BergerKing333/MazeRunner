import pygame
import numpy as np
from grid import grid
from mouse import mouse


class main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1300, 1300))
    pygame.display.set_caption("Maze Runner")

    running = True

    grid = grid(1300, 1300, screen.get_size(), seed_x=np.random.randint(0, 1000), seed_y=np.random.randint(0, 1000))

    mouse = mouse(grid, animate=True)
    path = []
    visited = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    grid.setStart(x, y)
                    mouse.clearPath(path)
                    mouse.clearPath(visited)


                elif event.button == 3:
                    if grid.start == None:
                        continue
                    x, y = pygame.mouse.get_pos()
                    grid.setEnd(x, y)
                    if grid.start != None:
                        path, visited = mouse.start(pathType="costmapAstar")
                        # mouse.drawVisited(visited)
                        mouse.drawPath(path)
                    # path = mouse.start()
                    # mouse.drawPath(path)
            # SEND THE OTHER EVENTS TO THE CONTROL HANDLER

        screen.fill((0, 0, 0))

        grid.draw(screen)
        pygame.display.flip()

        clock.tick(60)




if __name__ == "__main__":
    main()