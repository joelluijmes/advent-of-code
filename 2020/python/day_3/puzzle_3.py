from functools import reduce

with open("./day_3/data.txt") as f:
    pattern = f.read().splitlines()

limit_x = len(pattern[0])
limit_y = len(pattern)

# x = 0
# trees = 0
# for y in range(1, limit_y):
#     x = (x + 3) % limit_x
#     location = pattern[y][x]

#     if location == '#':
#         trees += 1

# print('Number of trees:', trees)

combinations = [
    # Right, down
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


def traverse_slope(right, down):
    trees = 0

    x = 0
    for y in range(down, limit_y, down):
        x = (x + right) % limit_x
        location = pattern[y][x]

        if location == "#":
            trees += 1

    return trees


multi_trees = reduce(
    lambda x, y: x * y, (traverse_slope(right, down) for right, down in combinations)
)
print(multi_trees)
