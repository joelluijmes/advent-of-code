import os


def read_battery_banks() -> list[str]:
    """Reads and parses the input.txt. Returns the battery banks."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]

    return lines


def find_max_combination(line: str, k: int) -> int:
    """Finds the maximum value in line, of maximum of k numbers in order e.g., 123491 -> 91 (k=2)"""

    def max_remaining_digit(sub: str, n: int):
        """Finds the maximum digit left in the sub string"""

        # max_digit is the current highest digit
        # pos is the position (zero based) where this was found
        max_digit, pos = 0, 0

        # Iterate through the rest of the string
        # k: fixed number of digits we want to have in our max value
        # n: controls the offset of the digit we are looking; this ensures we keep enough
        #    room for the remaining digits
        offset = max(0, k - n - 1)
        for i in range(len(sub) - offset):
            value = int(sub[i])
            if value > max_digit:
                max_digit = value
                pos = i

        return max_digit, pos + 1

    max_digit, pos = 0, 0
    total = ""
    for i in range(k):
        line = line[pos:]

        max_digit, pos = max_remaining_digit(line, i)
        total += str(max_digit)

    return int(total)


def main():
    battery_banks = read_battery_banks()

    k = 12
    max_values = [find_max_combination(line, k) for line in battery_banks]
    result = sum(max_values)

    print("Total: ", result)


if __name__ == "__main__":
    main()
