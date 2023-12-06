import re


def part1(s):
    total = 0

    for card in s:
        card = re.match(r"Card\s*\d+: (.*) \| (.*)", card)
        winning = set([int(n) for n in card.group(1).split()])
        have = set([int(n) for n in card.group(2).split()])
        winners = winning.intersection(have)

        value = 0
        for n in winners:
            if value == 0:
                value = 1
            else:
                value = value * 2

        total += value

    return total


def part2(s):
    totals = [1] * len(s)
    for i, card in enumerate(s):
        card = re.match(r"Card\s*\d+: (.*) \| (.*)", card)
        winning = set([int(n) for n in card.group(1).split()])
        have = set([int(n) for n in card.group(2).split()])
        winners = winning.intersection(have)

        for j in range(1, totals[i] + 1):
            for k in range(1, len(winners) + 1):
                totals[i + k] += 1
    return sum(totals)


with open("./inputs/day04", "r") as f:
    s = f.read()

s = s.strip().splitlines()

# print(part1(s))
print(part2(s))
