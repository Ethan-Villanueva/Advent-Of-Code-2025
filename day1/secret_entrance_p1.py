NUM_OF_DIALS = 100
point = 50
password = 0

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

print(password)