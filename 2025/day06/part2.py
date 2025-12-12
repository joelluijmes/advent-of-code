import os


def read_math_matrix() -> list[list[str]]:
    """Reads and parses the input.txt. Returns list of problems, taking into account the padding."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = [x.strip("\n\r") for x in fp.readlines()]

    # We need to determine the width of each column (including the padding). We can do this by looking
    # at the last line. The operation always is the first char in the column. We use this information
    # to determine the width.
    operations = lines[-1]

    widths = []
    counter = 0
    for char in operations[1:]:
        if char == " ":
            counter += 1
        else:
            widths.append(counter)
            counter = 0

    # Don't forget the last operation
    widths.append(counter + 1)

    # With the widths, we can parse the input column based, for every line read up to next column
    # no transposing of matrix needed
    matrix = []
    offset = 0
    for width in widths:
        op = lines[-1][offset : offset + width].strip()
        numbers = [line[offset : offset + width] for line in lines[:-1]]
        matrix.append(numbers + [op])

        offset += width + 1

    return matrix


def parse_cephalopod_math(matrix: list[list[str]]) -> list[list[str]]:
    """Parses the weird right to left, least significant version of numbers"""

    result = []

    # Example line: ['123', ' 45', '  6', '*']
    for line in matrix:
        rtl_numbers = []

        # Reverse iteration as we execute rtl
        for idx in range(len(line[0]) - 1, -1, -1):
            # For all numbers (columns), gather the current right most digit
            # merge it together to form the right to left digit
            number = "".join(col[idx] for col in line[:-1] if col[idx].strip())
            rtl_numbers.append(number)

        # Example output: ['356', '24', '1', '*']
        result.append(rtl_numbers + [line[-1]])

    return result


def main():
    math_matrix = read_math_matrix()

    cephalopod_matrix = parse_cephalopod_math(math_matrix)

    # Evaluate the problem line, last value is the operation, the rest are numbers
    # 1 2 3 + => eval(1+2+3)
    solutions = [eval(problem[-1].join(problem[:-1])) for problem in cephalopod_matrix]

    result = sum(solutions)
    print("Total: ", result)


if __name__ == "__main__":
    main()
