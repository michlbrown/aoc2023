import re


def part1(input):
    sum = 0
    for i, game in enumerate(input):
        matches = re.findall(r"((\d+) (\w*))", game)
        valid = True
        for m in matches:
            if m[2] == "red":
                if int(m[1]) > 12:
                    valid = False
            elif (m[2]) == "green":
                if int(m[1]) > 13:
                    valid = False
            elif (m[2]) == "blue":
                if int(m[1]) > 14:
                    valid = False

            if not valid:
                break

        if valid:
            sum += i + 1

    return sum


def part2(input):
    s = 0
    for i, game in enumerate(input):
        max_red = 0
        max_blue = 0
        max_green = 0
        grab = re.findall(r"((\d+) (\w*))", game)

        for dice in grab:
            n = int(dice[1])
            match dice[2]:
                case "red":
                    max_red = n if n > max_red else max_red
                case "green":
                    max_green = n if n > max_green else max_green
                case "blue":
                    max_blue = n if n > max_blue else max_blue

        power = max_red * max_green * max_blue
        s += power

    return s


with open("./inputs/day02") as f:
    input = f.read()

input = input.strip().split("\n")

print(part1(input))
print(part2(input))
