import os
from copy import deepcopy

SYMBOL_START = "S"
SYMBOL_EMPTY = "."
SYMBOL_SPLIT = "^"
SYMBOL_BEAM = "|"


def read_tachyon_manifold() -> list[list[str]]:
    """Reads and parses the input.txt. Returns 2D array representing the tachyon manifold."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/example.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]

    return [list(row) for row in lines]


def process_manifold(manifold: list[list[str]]) -> tuple[list[list[str]], int]:
    """Processes the beam through the manifold, while tracking the number of timelines.


    The approach is to accumulate the number of active timelines. E.g., every time a split
    happens, we sum the number to the 'top' left and right. Subsequently, each row in the
    manifold can then be accumulated to count the number of timelines active at that location.

    ['.', '.', '.', '.', '1', '.', '.', '.', '.']
    ['.', '.', '.', '.', '1', '.', '.', '.', '.']
    ['.', '.', '.', '1', '^', '1', '.', '.', '.']
    ['.', '.', '.', '1', '.', '1', '.', '.', '.']
    ['.', '.', '1', '^', '2', '^', '1', '.', '.']
    ['.', '.', '1', '.', '2', '.', '1', '.', '.']
    ['.', '1', '^', '3', '^', '3', '^', '1', '.']
    """

    result = deepcopy(manifold)

    # First find the start location of the beam
    start_idx = manifold[0].index(SYMBOL_START)

    # Set the first count to 1
    result[0][start_idx] = 1

    num_rows = len(manifold)
    num_cols = len(manifold[0])

    # Track the current beam locations
    active_beams = set([start_idx])

    # Iterate the beam through each of the layers
    for row in range(1, num_rows):
        for col in list(active_beams):
            if manifold[row][col] == SYMBOL_EMPTY:
                value = result[row - 1][col]

                # Beam passes freely through empty space
                if result[row][col] == SYMBOL_EMPTY:
                    result[row][col] = value

                # Otherwise we are on an overlapping path, thus append it
                else:
                    result[row][col] += value

            # Beam is split, and starts left/right
            elif manifold[row][col] == SYMBOL_SPLIT:
                active_beams.discard(col)

                if col > 0:
                    value = result[row - 1][col]

                    # Combine parallel paths of the top left value
                    if col - 1 > 0 and result[row][col - 1] != SYMBOL_EMPTY:
                        value += result[row][col - 1]

                    result[row][col - 1] = value
                    active_beams.add(col - 1)

                if col < num_cols:
                    value = result[row - 1][col]

                    # Combine parallel paths of the top right value
                    if col + 1 < num_cols and result[row][col + 1] != SYMBOL_EMPTY:
                        value += result[row][col + 1]

                    result[row][col + 1] = value
                    active_beams.add(col + 1)

    return result


def main():
    tachyon_manifold = read_tachyon_manifold()

    for line in tachyon_manifold:
        print(line)

    print()

    processed_manifold = process_manifold(tachyon_manifold)
    for line in processed_manifold:
        print([f"{x}" for x in line])

    result = sum(x for x in processed_manifold[-1] if isinstance(x, int))
    print("Total: ", result)


if __name__ == "__main__":
    main()
