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
    """Execute the rotations. Returns the real password, number of times dial passes at 0."""
    dial = dial_start
    real_password = 0

    for rot in rotations:
        passes = 0

        # When rotating left, we check if the rotation is larger then current dial, if so we pass the 0 mark.
        # E.g., 50 - 51 passes 0
        if rot < 0 and abs(rot) >= dial:
            # We calculate the distance to the next zero when rotating left (100 - dial), then we add the total
            # rotations beyond that crossing (+ abs(rot)). Subsequently we count how many rotations fit with // 100
            passes = (100 - dial + abs(rot)) // 100

            # When starting from zero, rotation is always larger than the dial value, however that is actually
            # not a real pass across zero
            if dial == 0:
                passes -= 1
        elif rot > 0:
            # Rotating right is easier, it just the amount of rotations that fit in total
            passes = (rot + dial) // 100

        real_password += passes
        dial = (dial + rot) % 100

    return real_password


def main():
    dial_start = 50

    rotations = read_rotations()
    print(rotations)

    real_pass = execute_rotations(dial_start, rotations)
    print("Real password: ", real_pass)


if __name__ == "__main__":
    main()
