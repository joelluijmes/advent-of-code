import os


def read_product_id_ranges() -> list[list[str]]:
    """Reads and parses the input.txt. Returns list of all product ids per range."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        range_line = fp.read()

    def parse_product_range(product_id_range: str) -> list[str]:
        """Explode range to all product ids"""
        start, end = product_id_range.split("-")
        start, end = int(start), int(end)

        return [str(x) for x in range(start, end + 1)]

    product_id_ranges = range_line.split(",")
    return [parse_product_range(x) for x in product_id_ranges]


def filter_product_id_range(product_ids: list[str]) -> list[int]:
    """Filters the product_ids for valid values. Invalid values are those with sequences repeated twice."""

    invalid_ids = set()

    for product_id in product_ids:
        sequence = str(product_id)

        for i in range(1, len(sequence)):
            value = sequence[:i]

            # Check if we have sequence of chars that might fit when repeated
            if len(sequence) % len(value) == 0:
                # Get the n times how much it would fit
                divisor = len(sequence) // len(value)
                repeated_value = value * divisor

                # if it actually is an id -> its invalid
                if repeated_value == product_id:
                    invalid_ids.add(product_id)

    return list(invalid_ids)


def accumulate_invalid_product_ids(product_id_ranges: list[list[str]]) -> int:
    total = 0

    for product_id_range in product_id_ranges:
        invalid_ids = filter_product_id_range(product_id_range)

        print(f"Range: {min(product_id_range)} - {max(product_id_range)}, invalids: {invalid_ids}")

        total += sum(int(x) for x in invalid_ids)

    return total


def main():
    product_id_ranges = read_product_id_ranges()
    result = accumulate_invalid_product_ids(product_id_ranges)

    print("Total: ", result)


if __name__ == "__main__":
    main()
