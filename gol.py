import random

alive = True
dead = False


def make_random_stage(size_of_grid):
    grid = []
    for i in range(size_of_grid):
        row = []
        for j in range(size_of_grid):
            row.append(random.randint(0, 1))
        grid.append(row)
    return grid


def print_grid(grid):
    print('\n')
    for i in grid:
        for j in i:
            print('# ', end='') if j == alive else print('. ', end='')
        print()


def get_number_of_neighbours_alive(state, i, j, size_of_grid):
    # I could refactor this part, there is a clever way to implement this function. I'll do it later.

    # First, exclude the corners.
    if i == 0 and j == 0:  # for the top left corner.
        return state[i + 1][j] + state[i][j + 1] + state[i + 1][j + 1]

    if i == size_of_grid - 1 and j == 0:  # for the bottom left corner.
        return state[i - 1][j] + state[i][j + 1] + state[i - 1][j + 1]

    if i == 0 and j == size_of_grid - 1:  # for the right top corner.
        return state[i][j - 1] + state[i + 1][j] + state[i+1][j - 1]

    if i == size_of_grid - 1 and j == size_of_grid - 1:  # for the bottom right corner.
        return state[i][j - 1] + state[i - 1][j] + state[i - 1][j - 1]

    # Now, extreme rows/columns.

    if i == 0:  # for the top row.
        return state[i][j - 1] + state[i][j + 1] + state[i + 1][j - 1] + state[i + 1][j] + state[i + 1][j + 1]

    if i == size_of_grid - 1:  # for the bottom row.
        return state[i][j - 1] + state[i][j + 1] + state[i - 1][j - 1] + state[i - 1][j] + state[i - 1][j + 1]

    if j == 0:  # for the left column.
        return state[i][j + 1] + state[i - 1][j] + state[i - 1][j + 1] + state[i + 1][j] + state[i + 1][j + 1]

    if j == size_of_grid - 1:  # for the right column.
        return state[i][j - 1] + state[i - 1][j] + state[i - 1][j - 1] + state[i + 1][j] + state[i + 1][j - 1]

    #  If it isn't any corner nor top/bottom column/row, we can just take all the neighbours.
    total = state[i - 1][j - 1] + state[i - 1][j] + state[i - 1][j + 1]
    total += state[i][j - 1] + state[i][j + 1]
    total += state[i + 1][j - 1] + state[i + 1][j] + state[i + 1][j + 1]
    return total


def evolve_state(state, size_of_grid):
    new_state = []
    for i in range(size_of_grid):
        new_state_row = []
        for j in range(size_of_grid):
            number_of_neighbours_alive = get_number_of_neighbours_alive(state, i, j, size_of_grid)

            new_state_of_cell = dead
            if state[i][j] == alive:
                new_state_of_cell = alive if number_of_neighbours_alive == 2 or number_of_neighbours_alive == 3 \
                    else dead
            else:
                new_state_of_cell = alive if number_of_neighbours_alive == 3 else dead
            new_state_row.append(new_state_of_cell)

        new_state.append(new_state_row)
    return new_state
