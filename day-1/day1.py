def main():

    operations = []
    number = 50
    password = 0

    with open("day1.txt") as document:
        for rotation in document:
            mult = 1
            if rotation[0] == 'L':
                mult = -1
            operations.append(mult * int(rotation[1:]))

    for op in operations:
        number = (number + op) % 100
        if number == 0:
            password += 1

    print("Part 1:", password)

    password = 0
    number = 50

    for op in operations:
        if op < 0 and number > 0:
            diff = abs(op) - number
        else:
            diff = abs(op) - (100 - number)
        if diff >= 0:
            password += 1 + diff // 100
        number = (number + op) % 100
    print("Part 2:", password)

if __name__=="__main__":
    main()