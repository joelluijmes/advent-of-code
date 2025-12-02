import string

from functools import reduce
from collections import Counter

with open("./day_6/data.txt") as f:
    groups = f.read().split("\n\n")

# group_answers = [set(c for c in group if c in string.ascii_lowercase) for group in groups]
# total_answers = reduce(lambda x, y: x + len(y), group_answers, 0)
# print(total_answers)

group_answers = [group.splitlines() for group in groups]


def count_answer(group):
    n = len(group)

    counts = Counter([x for x in group for x in list(x)])
    return sum(1 if count == n else 0 for count in counts.values())


total_answers = sum(count_answer(group) for group in group_answers)
print(total_answers)
