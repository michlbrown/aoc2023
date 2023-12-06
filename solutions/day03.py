def is_symbol(c):
    if c.isdigit():
        return False
    elif c == ".":
        return False
    else:
        return True


def search_valid(s, i, j):
    # top
    if i > 0:
        # top left
        if j > 0 and is_symbol(s[i - 1][j - 1]):
            return True
        # top right
        if j < (len(s[i]) - 1) and is_symbol(s[i - 1][j + 1]):
            return True
        # top middle
        if is_symbol(s[i - 1][j]):
            return True

    # left
    if j > 0 and is_symbol(s[i][j - 1]):
        return True

    # below
    if i < (len(s) - 1):
        # bot left
        if j > 0 and is_symbol(s[i + 1][j - 1]):
            return True
        # bot right
        if j < (len(s) - 1) and is_symbol(s[i + 1][j + 1]):
            return True
        # bot mid
        if is_symbol(s[i + 1][j]):
            return True

    # right
    if j < (len(s) - 1) and is_symbol(s[i][j + 1]):
        return True

    return False


def search_gear(s, i, j):
    # top
    if i > 0:
        # top left
        if j > 0 and (s[i - 1][j - 1] == "*"):
            return (i - 1, j - 1)
        # top right
        if j < (len(s[i]) - 1) and (s[i - 1][j + 1] == "*"):
            return (i - 1, j + 1)
        # top middle
        if s[i - 1][j] == "*":
            return (i - 1, j)

    # left
    if j > 0 and (s[i][j - 1] == "*"):
        return (i, j - 1)

    # below
    if i < (len(s) - 1):
        # bot left
        if j > 0 and (s[i + 1][j - 1] == "*"):
            return (i + 1, j - 1)
        # bot right
        if j < (len(s) - 1) and (s[i + 1][j + 1] == "*"):
            return (i + 1, j + 1)
        # bot mid
        if s[i + 1][j] == "*":
            return (i + 1, j)
    # right
    if j < (len(s) - 1) and is_symbol(s[i][j + 1]):
        return (i, j + 1)

    return None


def part1(s):
    r = 0
    for i in range(0, len(s)):
        in_num = False
        valid = False
        n = None
        for j in range(0, len(s[i])):
            c = s[i][j]
            if c.isdigit() and not in_num:
                n = c
                in_num = True
                valid = search_valid(s, i, j)
            elif c.isdigit() and in_num:
                n = n + c
                valid = valid or search_valid(s, i, j)
            elif in_num:
                if valid:
                    r += int(n)
                n = None
                in_num = False
            else:
                in_num = False

        if in_num and valid:
            r += int(n)

    return r


def part2(s):
    gears = {}
    for i in range(0, len(s)):
        in_num = False
        valid = None
        n = None
        g = set()
        for j in range(0, len(s[i])):
            c = s[i][j]
            if c.isdigit() and not in_num:  # beginning of number
                n = c
                in_num = True
                gear = search_gear(s, i, j)
                if gear is not None:
                    valid = True
                    g.add(gear)
            elif c.isdigit() and in_num:  # within number
                n = n + c
                gear = search_gear(s, i, j)
                if gear is not None:
                    valid = True
                    g.add(gear)
            elif in_num:  # after number
                if valid:
                    for x in g:
                        if x in gears:
                            gears[x].append(n)
                        else:
                            gears[x] = [n]

                    g.clear()
                n = None
                # g.clear()
                in_num = False

        if in_num and valid:  # after number at end of line
            for x in g:
                if x in gears:
                    gears[x].append(n)
                else:
                    gears[x] = [n]

    sum = 0
    for gear, parts in gears.items():
        if len(parts) == 2:
            sum += int(parts[0]) * int(parts[1])

    return sum


with open("./inputs/day03") as f:
    s = f.read()

s = [list(line) for line in s.strip().split("\n")]
# print(part1(s))
print(part2(s))
