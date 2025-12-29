invalid_IDs = []

def part1():
    global invalid_IDs
    with open("day2_input.txt", "r") as f:
        ranges = f.read().split(',')
        for ID_range in ranges:
            start, end = ID_range.split('-')
            for i in range(int(start), int(end)+1):
                digits = str(i)

                if len(digits) % 2 == 1: continue
                else:
                    half_way = len(digits)//2
                    first_half = digits[0:half_way]
                    second_half = digits[half_way:]

                    if first_half == second_half:
                        invalid_IDs.append(int(digits))
    
    f.close()    
    print(sum(invalid_IDs))

def part2():
    global invalid_IDs
    with open("day2_input.txt", "r") as f:
        ranges = f.read().split(',')
        for ID_range in ranges:
            start, end = ID_range.split('-')
            for i in range(int(start), int(end)+1):
                digits = str(i)

                seen = ""
                for i in range((len(digits)//2) + 1):
                    repeated = digits.count(seen) 
                    if repeated >= 2 and len(digits) == repeated * len(seen):
                        invalid_IDs.append(int(digits))
                        break
                    else: seen += digits[i]

    f.close()
    print(sum(invalid_IDs))

part2()