import os


def read_math_matrix() -> list[list[str]]:
    """Reads and parses the input.txt. Returns list of problems."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]

    # The math line is splitted by number of spaces. Python doesn't really
    # care about the amount of spaces, split just takes all of them.
    matrix = [row.split() for row in lines]

    # Transpose the matrix
    transposed = zip(*matrix)
    return transposed


def main():
    math_matrix = read_math_matrix()

    # Evaluate the problem line, last value is the operation, the rest are numbers
    # 1 2 3 + => eval(1+2+3)
    solutions = [eval(problem[-1].join(problem[:-1])) for problem in math_matrix]

    result = sum(solutions)
    print("Total: ", result)


if __name__ == "__main__":
    main()
