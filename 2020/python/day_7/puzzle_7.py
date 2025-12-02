import re

with open("./day_7/data.txt") as f:
    rules = f.read().splitlines()


def parse_rule(line: str):
    match_bag_name = re.match(r"^(\w+\s\w+) bags? contain ", line)
    assert match_bag_name is not None

    bag_name = match_bag_name.group(1)

    match_subbags = re.findall(r"(\d+) (\w+\s\w+) bags?", line)
    subbags = dict((bag, int(count)) for count, bag in match_subbags)

    return (bag_name, subbags)


rules = dict(parse_rule(line) for line in rules)


def find_all_parents(target, result=set()):

    parents = [bag for bag, subbags in rules.items() if target in subbags]
    result.update(parents)

    for parent in parents:
        find_all_parents(parent, result)

    return result


parents = find_all_parents('shiny gold')
print('Number of bags which may contain shiny gold', len(parents))


def sum_subbags(target):
    return sum(count + count * sum_subbags(bag) for bag, count in rules[target].items())

result = sum_subbags('shiny gold')
print('Sum of subbags which shiny gold holds', result)
