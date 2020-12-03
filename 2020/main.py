import re

def day_1_input(numbers):
    """
    Find 2 entries that sum to 2020
    return their product
    """
    m = {}
    for n in numbers:
        if n in m:
            return n*m[n]
        else:
            m[2020-n] = n

    return None


def day_1_part_2(numbers):
    """
    Find 3 entries that sum to 2020
    return their product
    """
    m = {}
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            n = numbers[i]
            if n in m:
                return n * m[n][0] * m[n][1]

            x = numbers[i]
            y = numbers[j]
            if x + y < 2020:
                m[2020 - (x+y) ] = [ x, y]

    return None


def day_2_count_valid_passwords(entries):
    count = 0

    for entrie in entries:
        m = re.search(r'(\d+)-(\d+) (.): (\w+)', entrie)
        password = m.group(4)
        char = m.group(3)
        lower, upper = m.group(1), m.group(2)

        if int(lower) <= password.count(char) <= int(upper):
            count += 1

    return count


def day_2_count_valid_passwords_part_2(entries):
    count = 0

    for entrie in entries:
        m = re.search(r'(\d+)-(\d+) (.): (\w+)', entrie)
        password = m.group(4)
        char = m.group(3)
        i, j = int(m.group(1))-1, int(m.group(2))-1

        if (password[i] == char) != (password[j] == char): # hacky way to do XOR
            count += 1

    return count


def day1():
    numbers = []
    with open('day_1_input.txt') as f:
        for line in f:
            numbers.append(int(line))

    print(day_1_input(numbers))
    print(day_1_part_2(numbers))


def day2():
    passwords = []
    with open('day_2_input.txt') as f:
        for line in f:
            passwords.append(line)

    print(day_2_count_valid_passwords(passwords))

    print(day_2_count_valid_passwords_part_2(passwords))


def day_3_part1(map, slope):
    di, dj = slope
    count = 0
    i, j = 0, 0
    m = len(map[0])
    while i < len(map):
        if map[i][j] == '#':
            count += 1
        i += di
        j = (j + dj) % m

    return count


def day3():
    #with open('test.txt') as f:
    with open('day_3_input.txt') as f:
        map = [[c for c in line.rstrip()] for line in f]

    print(day_3_part1(map, slope=(1, 3)))

    result = 1
    for slope in [ (1,1), (1,3), (1,5), (1,7), (2,1) ]:
        result *= day_3_part1(map, slope)

    print(result)

day3()
