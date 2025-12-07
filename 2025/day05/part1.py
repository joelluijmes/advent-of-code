import os


def read_ingredients() -> tuple[list[tuple[int, int]], list[int]]:
    """Reads and parses the input.txt. Returns list of fresh product id ranges, and available product ids."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]

    parsing_ranges = True

    fresh_product_id_ranges = []
    available_product_ids = []

    for line in lines:
        # empty line indicates switch
        if parsing_ranges and not line:
            parsing_ranges = False
            continue

        if parsing_ranges:
            bits = line.split("-")
            start, end = int(bits[0]), int(bits[1]) + 1

            fresh_product_id_ranges.append((start, end))

        # else we are parsing available product ids
        else:
            value = int(line)
            available_product_ids.append(value)

    return fresh_product_id_ranges, available_product_ids


def main():
    fresh_product_id_ranges, available_product_ids = read_ingredients()

    # Count product_ids which are in valid range
    result = sum(1 for product_id in available_product_ids if any(start <= product_id <= end for start, end in fresh_product_id_ranges))

    print("Total: ", result)


if __name__ == "__main__":
    main()
