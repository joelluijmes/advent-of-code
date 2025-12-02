with open("./day_5/data.txt") as f:
    seats = f.read().splitlines()

rows = 128
columns = 8


def decode_seat(encoded_seat: str):
    assert len(encoded_seat) == 10

    def decode(input: str, char_left, char_right, upper):
        lower = 0
        upper -= 1

        for i in range(len(input)):
            if input[i] == char_left:
                upper = lower + (upper - lower) // 2
            elif input[i] == char_right:
                lower = 1 + lower + (upper - lower) // 2
            else:
                raise ValueError("Something aint right..")

        assert lower == upper
        return lower

    row = decode(encoded_seat[:7], "F", "B", rows)
    column = decode(encoded_seat[7:], "L", "R", columns)

    return (row, column, row * 8 + column)


decoded_seats = [decode_seat(seat) for seat in seats]
sorted_seats = sorted(decoded_seats, key=lambda seat: seat[2])
print("Maximum seat", sorted_seats[-1])

seat_ids = [seat[2] for seat in sorted_seats]
missing_id = next(
    index
    for index, id in enumerate(seat_ids)
    if index < len(seat_ids) and seat_ids[index + 1] != id + 1
)
print("Missing id", seat_ids[missing_id] + 1)
