import os

PAPER_ROLL = "@"
ACCESSIBLE = "x"
EMPTY_SPACE = "."


def read_paper_grid() -> list[list[str]]:
    """Reads and parses the input.txt. 2D array representing the grid."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = fp.readlines()

    return [list(row.strip()) for row in lines]


def find_accessible_spots(grid: list[str]):
    len_rows = len(grid)
    len_cols = len(grid[0])

    # Create result grid, note we cannot nest [..] * syntax as it refers to the same list
    result = [[EMPTY_SPACE] * len_cols for _ in range(len_rows)]

    for y in range(len_rows):
        for x in range(len_cols):
            value = grid[y][x]

            if value != PAPER_ROLL:
                result[y][x] = value
                continue

            directions = [
                (-1, 0),  # top
                (-1, 1),  # top-right
                (0, 1),  # right
                (1, 1),  # bottom-right
                (1, 0),  # bottom
                (1, -1),  # bottom-left
                (0, -1),  # left
                (-1, -1),  # top-left
            ]

            # Consider all valid surrounding values
            surroundings = [grid[y + ny][x + nx] for ny, nx in directions if 0 <= y + ny < len_rows and 0 <= x + nx < len_cols]

            totals = sum(1 for x in surroundings if x == PAPER_ROLL)
            if totals < 4:
                result[y][x] = ACCESSIBLE
            else:
                result[y][x] = value

    return result


def main():
    grid = read_paper_grid()
    for line in grid:
        print(line)

    print()

    result = find_accessible_spots(grid)
    for line in result:
        print(line)

    result = sum(sum(1 for col in row if col == ACCESSIBLE) for row in result)

    print("Total: ", result)


if __name__ == "__main__":
    main()
