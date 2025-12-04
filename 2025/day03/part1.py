import os


def read_battery_banks_max_jolts() -> list[str]:
    """Reads and parses the input.txt. Returns per line maximum number of jolts."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = fp.readlines()

    def find_max_joltage(line: str) -> int:
        current_max = 0

        # The max number of jolts is the number with two largest digits, without rearranging
        # 71119 -> 79
        for i in range(len(line)):
            for j in range(i + 1, len(line) - 1):
                value = int(line[i] + line[j])

                if value > current_max:
                    current_max = value

        return current_max

    return [find_max_joltage(line) for line in lines]


def main():
    battery_banks_max_jolts = read_battery_banks_max_jolts()
    result = sum(battery_banks_max_jolts)

    print("Total: ", result)


if __name__ == "__main__":
    main()
