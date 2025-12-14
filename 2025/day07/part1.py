import os
from copy import deepcopy

SYMBOL_START = "S"
SYMBOL_EMPTY = "."
SYMBOL_SPLIT = "^"
SYMBOL_BEAM = "|"


def read_tachyon_manifold() -> list[list[str]]:
    """Reads and parses the input.txt. Returns 2D array representing the tachyon manifold."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]

    return [list(row) for row in lines]


def process_manifold(manifold: list[list[str]]) -> tuple[list[list[str]], int]:
    """Processes the beam through the manifold, while tracking the number of splits."""

    result = deepcopy(manifold)

    # First find the start location of the beam
    start_idx = manifold[0].index(SYMBOL_START)

    num_rows = len(manifold)
    num_cols = len(manifold[0])

    # Track the previous level starting beam points
    previous_beams = set([start_idx])
    split_counter = 0

    # Iterate the beam through each of the layers
    for row in range(1, num_rows):
        for col in list(previous_beams):
            # Beam passes freely through empty space
            if manifold[row][col] == SYMBOL_EMPTY:
                result[row][col] = SYMBOL_BEAM

            # Beam is stopped, and starts left/right
            elif manifold[row][col] == SYMBOL_SPLIT:
                previous_beams.discard(col)

                if col > 0:
                    result[row][col - 1] = SYMBOL_BEAM
                    previous_beams.add(col - 1)
                if col < num_cols:
                    result[row][col + 1] = SYMBOL_BEAM
                    previous_beams.add(col + 1)

                split_counter += 1

    return result, split_counter


def main():
    tachyon_manifold = read_tachyon_manifold()

    for line in tachyon_manifold:
        print(line)

    print()

    beamed_manifold, split_counter = process_manifold(tachyon_manifold)
    for line in beamed_manifold:
        print(line)

    print("Total: ", split_counter)


if __name__ == "__main__":
    main()
