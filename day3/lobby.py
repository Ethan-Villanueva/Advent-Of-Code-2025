def part1():
    total = 0
    with open("day3_input.txt", "r") as f:
        for bank in f:
            max_volts = 0

            volts = list(map(int, bank.strip()))
            for i in range(len(volts)-1):
                first_index = volts[i]
                max_second = max(volts[i+1:])

                v = first_index * 10 + max_second
                max_volts = max(max_volts, v)

            total += max_volts

    print(total)

part1()