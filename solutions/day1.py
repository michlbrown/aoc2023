f = open("./inputs/day01", "r")


m = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

sum = 0
for line in f:
    first = None
    last = None
    w = ""
    for c in line:
        if c.isdigit():
            last = c
            if first is None:
                first = c
        else:
            w += c
            for k, v in m.items():
                if w.endswith(k):
                    last = v

                    if first is None:
                        first = v

    sum += int(first + last)

print(sum)
