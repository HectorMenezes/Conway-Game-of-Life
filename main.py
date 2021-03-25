import gol as gol
import pygame
import time

# We'll have a nxn game.
size_of_grid = 40

# Initialize pygame and make a display with a white background.
size_of_screen = 1000
pygame.init()
screen = pygame.display.set_mode((size_of_screen, size_of_screen))
screen.fill((255, 255, 255))

# Draw the lines.
margin = 20
size_of_cell = (size_of_screen - 2 * margin) / size_of_grid

black = (0, 0, 0)
for i in range(size_of_grid + 1):
    pygame.draw.line(screen, black, (margin + i * size_of_cell, margin),
                     (margin + i * size_of_cell, size_of_screen - margin))
    pygame.draw.line(screen, black, (margin, margin + i * size_of_cell),
                     (size_of_screen - margin, margin + i * size_of_cell))

# Title and icon
pygame.display.set_caption('Game of Life')
pygame.display.set_icon(pygame.image.load('./images/Icon.png'))  # I don't know if that is working properly,
# my distro doesnt' show the icon haha

# Set icons for living cells and dead ones
icon_size = int(size_of_cell - 6)
cell_icon = pygame.transform.smoothscale(pygame.image.load('./images/cell.png'), (icon_size, icon_size))
skull_icon = pygame.transform.smoothscale(pygame.image.load('./images/skull.png'), (icon_size, icon_size))


def get_coordinates():  # Get coordinates of the grid, we'll use it to change/set icons.
    coordinates = []
    for i in range(size_of_grid):
        row = []
        for j in range(size_of_grid):
            row.append([23 + i * size_of_cell, 23 + j * size_of_cell])
        coordinates.append(row)
    return coordinates


def change_icons(size_of_grid, state, coord):  # Change the icons according to a matrix of a state.
    for i in range(size_of_grid):
        for j in range(size_of_grid):
            if state[i][j]:
                screen.blit(cell_icon, (coord[i][j][0], coord[i][j][1]))
            else:
                screen.blit(skull_icon, (coord[i][j][0], coord[i][j][1]))


def clean_screen(coord):  # Fill places with blank spaces before we change.
    screen.fill((255, 255, 255))
    for i in range(size_of_grid + 1):
        pygame.draw.line(screen, black, (margin + i * size_of_cell, margin),
                         (margin + i * size_of_cell, size_of_screen - margin))
        pygame.draw.line(screen, black, (margin, margin + i * size_of_cell),
                         (size_of_screen - margin, margin + i * size_of_cell))


# Initial state:
current_state = gol.make_random_stage(size_of_grid)
coord = get_coordinates()
change_icons(size_of_grid, current_state, coord)
pygame.display.update()

time.sleep(1)

# Loop of Game of Life
running = True
while running:
    time.sleep(0.2)
    clean_screen(coord)
    current_state = gol.evolve_state(current_state, size_of_grid)
    change_icons(size_of_grid, current_state, coord)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
