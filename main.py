import gol as gol
import pygame
import time

# We'll have a 10x10 game.
size_of_grid = 10

# Initialize pygame and make a display with a white background.
pygame.init()
screen = pygame.display.set_mode((800, 800))
screen.fill((255, 255, 255))

# Draw the lines.
margin = 20
black = (0, 0, 0)
for i in range(11):
    pygame.draw.line(screen, black, (20 + i * 76, 20), (20 + i * 76, 780))
    pygame.draw.line(screen, black, (20, 20 + i * 76), (780, 20 + i * 76))

# Title and icon
pygame.display.set_caption('Game of Life')
pygame.display.set_icon(pygame.image.load('./images/Icon.png'))  # I don't know if that is working properly,
# my distro doesnt' show the icon haha

# Set icons for living cells and dead ones
icon_size = 70
cell_icon = pygame.transform.smoothscale(pygame.image.load('./images/cell.png'), (icon_size, icon_size))
skull_icon = pygame.transform.smoothscale(pygame.image.load('./images/skull.png'), (icon_size, icon_size))


def get_coordinates():  # Get coordinates of the grid, we'll use it to change/set icons.
    coordinates = []
    for i in range(10):
        row = []
        for j in range(10):
            row.append([23 + i * 76, 23 + j * 76])
        coordinates.append(row)
    return coordinates


def change_icons(size_of_grid, state, coord):  # Change the icons according to a matrix of a state.
    for i in range(size_of_grid):
        for j in range(size_of_grid):
            if state[i][j]:
                screen.blit(cell_icon, (coord[i][j][0], coord[i][j][1]))
            else:
                screen.blit(skull_icon, (coord[i][j][0], coord[i][j][1]))


def clean_icons(coord):  # Fill places with blank spaces before we change.
    for i in range(size_of_grid):
        for j in range(size_of_grid):
            pygame.draw.rect(screen, (255, 255, 255), (coord[i][j][0], coord[i][j][1], 72, 72))


# Initial state:
current_state = gol.make_random_stage(size_of_grid)
coord = get_coordinates()
change_icons(size_of_grid, current_state, coord)
pygame.display.update()

# Loop of Game of Life
running = True
while running:
    time.sleep(1)
    clean_icons(coord)
    current_state = gol.evolve_state(current_state, size_of_grid)
    change_icons(size_of_grid, current_state, coord)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

