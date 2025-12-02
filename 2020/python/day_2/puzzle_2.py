import re

regex = re.compile(r"(\d+)\-(\d+) (\w): (\w+)")

with open("./day_2/data.txt") as f:
    inputs = f.read().splitlines()


def is_valid_count(input: str):
    min_str, max_str, char, password = regex.findall(input)[0]
    occurences = password.count(char)

    return int(min_str) <= occurences <= int(max_str)


no_valid_count = sum(1 if is_valid_count(input) else 0 for input in inputs)
print("Valid based on count", no_valid_count)


def is_valid_indexed(input: str):
    min_str, max_str, char, password = regex.findall(input)[0]
    min_index, max_index = int(min_str), int(max_str)

    min_match = len(password) >= min_index and password[min_index - 1] == char
    max_match = len(password) >= max_index and password[max_index - 1] == char

    return min_match ^ max_match


no_valid_indexed = sum(1 if is_valid_indexed(input) else 0 for input in inputs)
print("Valid based on char match", no_valid_indexed)
