import itertools

with open("./day_10/data.txt") as f:
    numbers = sorted(int(x) for x in f.read().splitlines())


current = 0
count_single = 0
count_triple = 0
for number in numbers:
    if max(0, current - 1) <= number <= current + 1:
        current = number
        count_single += 1
    elif max(0, current - 3) <= number <= current + 3:
        current = number
        count_triple += 1
    else:
        break

max_jolts = current + 3
count_triple += 1

print('Singles', count_single, 'Triples', count_triple, 'Result', count_single*count_triple, 'Max jolts', max_jolts)


# part two
result = {0: 1}
for number in numbers:
    result[number] = 0
    if number - 1 in result:
        result[number] += result[number-1]
    if number - 2 in result:
        result[number] += result[number-2]
    if number - 3 in result:
        result[number] += result[number-3]

print('Valid combinations', result[max(numbers)])