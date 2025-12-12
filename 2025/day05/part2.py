import os


def read_product_id_ranges() -> list[tuple[int, int]]:
    """Reads and parses the input.txt. Returns list of fresh product id ranges."""

    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(f"{current_dir}/input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]

    fresh_product_id_ranges = []

    for line in lines:
        # empty line indicates switch, for this part 2 we can stop. Only ranges are relevant
        if not line:
            return fresh_product_id_ranges

        bits = line.split("-")
        start, end = int(bits[0]), int(bits[1])

        fresh_product_id_ranges.append((start, end))


def distinct_ranges(ranges: list[tuple[int, int]]):
    """Makes all ranges distinctive, e.g., without overlaps."""
    ranges = sorted(ranges)

    distinctive_ranges = []

    for id_range in ranges:
        current_min, current_max = id_range
        previous_min, previous_max = distinctive_ranges[-1] if distinctive_ranges else (0, 0)

        # Only consider current range if it even exceeds the previous one; otherwise it is
        # already contained e.g., 1-5; 2-3 => 1-5
        if current_max > previous_max:
            # If the current range is larger than the previous, just add it as is
            if current_min > previous_max:
                distinctive_ranges.append((current_min, current_max))

            # Otherwise, we have an overlapping range we need to distinctivy
            # e.g., 2-5; 4-7 => 2-5; 6-7
            elif current_min <= previous_max:
                distinctive_ranges.append((previous_max + 1, current_max))

    return distinctive_ranges


def main():
    fresh_product_id_ranges = read_product_id_ranges()
    result = distinct_ranges(fresh_product_id_ranges)

    # Accumulate the total length
    result = sum(end - start + 1 for start, end in result)
    print("Total: ", result)


if __name__ == "__main__":
    main()
