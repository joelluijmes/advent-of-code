# Parsing the data seems impractical (if not impossible) to do in SQL, there for this file will
# generate the data for SQL in normalized form.

import re

with open("../python/day_7/data.txt") as f:
    rules = f.read().splitlines()


def parse_rule(line: str):
    match_bag_name = re.match(r"^(\w+\s\w+) bags? contain ", line)
    assert match_bag_name is not None

    bag_name = match_bag_name.group(1)

    match_subbags = re.findall(r"(\d+) (\w+\s\w+) bags?", line)
    subbags = dict((bag, int(count)) for count, bag in match_subbags)

    return (bag_name, subbags)


rules = dict(parse_rule(line) for line in rules)

lines = []
for bag, subbags in rules.items():
    for subbag, count in subbags.items():
        lines.append(
            f'    STRUCT("{bag}" AS bag, "{subbag}" AS subbag, {count} AS num),\n'
        )

# Drops the trailing comma
lines[-1] = lines[-1][:-2]

with open("./seed.txt", "w") as f:
    f.write(f"CREATE OR REPLACE TABLE joell-dev.aoc_2020.data_7 AS (\n")
    f.write(f"SELECT x.* FROM UNNEST([\n")
    f.writelines(lines)
    f.write("]) x\n);")
