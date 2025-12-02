with open("./day_1/data.txt") as f:
    expense_report = [int(x) for x in f.read().splitlines()]

max_value = max(
    x * y  # generate all combinations of unordered set
    for x in expense_report
    for y in expense_report
    if x > y and x + y == 2020
)
print("Part 1", max_value)

max_value = max(
    x * y * z
    for x in expense_report
    for y in expense_report
    for z in expense_report
    if x > y and y > z and x + y + z == 2020
)
print("Part 2", max_value)
