NUM_OF_DIALS = 100
point = 50
password = 0

def part1():
    global point,password
    with open("day1_input.txt", "r") as f:
        for line in f:
            direction = line[0]
            clicks = int(line[1:])

            if line[0] == 'L':
                point -= clicks
            else:
                point += clicks
            
            point %= NUM_OF_DIALS
            if point == 0:
                password += 1

    f.close()
    print(password)

def part2():
    global point,password
    with open("day1_input.txt", "r") as f:
        for line in f:
            direction = line[0]
            clicks = int(line[1:])

            full_rots = clicks // NUM_OF_DIALS
            password += full_rots
            clicks %= NUM_OF_DIALS
            if direction == 'L':
                if clicks >= point:
                    password += 1
                point -= clicks
            else:
                if clicks >= NUM_OF_DIALS - point:
                    password += 1
                point += clicks

            point %= NUM_OF_DIALS

    f.close()
    print(password)