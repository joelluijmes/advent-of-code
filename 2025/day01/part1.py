import os


def read_rotations() -> list[int]:
    """Reads and parses the input.txt. Returns full list of rotations to take."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        rotations = fp.readlines()

    def parse_rotation(rotation: str) -> int:
        """Converts line to number e.g., L68 -> -68 and R42 -> 42"""
        direction, amount = rotation[0], int(rotation[1:])
        return amount if direction == "R" else amount * -1

    return [parse_rotation(x) for x in rotations]


def execute_rotations(dial_start: int, rotations: list[int]) -> int:
    """Execute the rotations. Returns the real password, number of times dial ends up at 0."""
    dial = dial_start
    real_password = 0

    for x in rotations:
        dial = (dial + x) % 100

        if dial == 0:
            real_password += 1

    return real_password


def main():
    dial_start = 50

    rotations = read_rotations()
    print(rotations)

    real_pass = execute_rotations(dial_start, rotations)
    print("Real password: ", real_pass)


if __name__ == "__main__":
    main()
