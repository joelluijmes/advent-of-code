from itertools import combinations

with open("./day_9/data.txt") as f:
    numbers = [int(x) for x in f.read().splitlines()]


def find_missing():
    preamble = 25
    for i in range(preamble, len(numbers) - 1):

        found = False
        for x, y in combinations(numbers[i-preamble:i], 2):
            if x + y == numbers[i]:
                found = True
                break

        if not found:
            return numbers[i]

    return None


print(find_missing())


def find_contiguous(num=1504371145):
    return next(
        min(numbers[i:j]) + max(numbers[i:j])
        for i in range(len(numbers))
        for j in range(i, len(numbers))
        if sum(numbers[i:j]) == num
    )


print(find_contiguous())
