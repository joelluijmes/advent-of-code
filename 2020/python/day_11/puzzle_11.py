with open("./day_11/data.txt") as f:
    seats = [list(line) for line in f.read().splitlines()]

rows = len(seats)
cols = len(seats[0])


def iterate(seats, window_func, threshold):
    changed = False
    result = [[None]*rows for x in range(cols)]
    for y in range(rows):
        for x in range(cols):
            windowed = window_func(seats, y, x)
            count_occupied = sum(1 if x == '#' else 0 for x in windowed)
            seat = seats[y][x]

            if seat == 'L':
                if count_occupied == 0:
                    result[y][x] = '#'
                    changed = True
                else:
                    result[y][x] = 'L'
            elif seat == '#':
                if count_occupied >= threshold:
                    result[y][x] = 'L'
                    changed = True
                else:
                    result[y][x] = '#'
            elif seat == '.':
                result[y][x] = '.'

    return result, changed


def run(window_func, threshold):
    counter = 0
    result = [row[:] for row in seats]
    while True:
        result, changed = iterate(result, window_func, threshold)
        if not changed:
            break

        counter += 1

    total_seats = sum(1 if seat == '#' else 0 for row in result for seat in row)
    print('Stabilized after rounds', counter, 'seats taken', total_seats)


print('Part 1')
run(lambda seats, x, y: [
    item
    for sublist in [sub[max(0, x-1):x+2] for sub in seats[max(0, y-1):y+2]]
    for item in sublist
], threshold=4)


print('Part 2')


def rayed_window(seats, row, col):
    rows = len(seats)
    cols = len(seats[0])

    return [
        next((seats[row-i][col] for i in range(1, row + 1) if seats[row-i][col] != '.'), 'x'),
        next((seats[row-i][col+i] for i in range(1, min(row + 1, cols - col)) if seats[row-i][col+i] != '.'), 'x'),
        next((seats[row][col+i] for i in range(1, cols - col) if seats[row][col+i] != '.'), 'x'),
        next((seats[row+i][col+i] for i in range(1, min(cols, rows) - max(col, row)) if seats[row+i][col+i] != '.'), 'x'),
        next((seats[row+i][col] for i in range(1, rows - row) if seats[row+i][col] != '.'), 'x'),
        next((seats[row+i][col-i] for i in range(1, min(col + 1, rows - row)) if seats[row+i][col-i] != '.'), 'x'),
        next((seats[row][col-i] for i in range(1, col + 1) if seats[row][col-i] != '.'), 'x'),
        next((seats[row-i][col-i] for i in range(1, min(col + 1, row + 1)) if seats[row-i][col-i] != '.'), 'x'),
    ]


run(rayed_window, threshold=5)
