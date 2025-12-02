import re

field_matcher = re.compile(r"((\w+):([\S]+))[\s\n]*")

with open("./day_4/data.txt") as f:
    passports = f.read().split("\n\n")

# def is_valid(passport: str) -> bool:
#     required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
#     passport_fields = dict((key, value) for _, key, value in field_matcher.findall(passport))

#     return all(field in passport_fields for field in required_fields)


def is_valid(passport: str) -> bool:
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    passport_fields = dict(
        (key, value) for _, key, value in field_matcher.findall(passport)
    )

    has_required_fields = all(field in passport_fields for field in required_fields)
    if not has_required_fields:
        return False

    def is_valid_field(field, value):
        if field == "byr":
            return 1920 <= int(value) <= 2002
        elif field == "iyr":
            return 2010 <= int(value) <= 2020
        elif field == "eyr":
            return 2020 <= int(value) <= 2030
        elif field == "hgt":
            if value[-2:] == "in":
                return 59 <= int(value[:-2]) <= 76
            elif value[-2:] == "cm":
                return 150 <= int(value[:-2]) <= 193
        elif field == "hcl":
            return re.match(r"^#[\da-f]{6}$", value) is not None
        elif field == "ecl":
            return value in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
        elif field == "pid":
            return re.match(r"^\d{9}$", value) is not None
        elif field == "cid":
            return True

        return False

    return all(is_valid_field(field, value) for field, value in passport_fields.items())


valid_passports = sum(1 if is_valid(passport) else 0 for passport in passports)
print("Valid passports:", valid_passports)
