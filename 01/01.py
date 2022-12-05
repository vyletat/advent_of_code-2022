f = open("input.txt", "r")
elf = []

calories_sum = 0
# read input and if there is number add it to total and if not read next line and add total to elf
for line in f:
    line = line.strip()
    if line.isdigit():
        calories_sum += int(line)
    else:
        elf.append(calories_sum)
        calories_sum = 0
        continue
elf.append(calories_sum)
print(max(elf))

# find 3 max numbers in elf and sum them
elf.sort(reverse=True)
print(elf[0] + elf[1] + elf[2])
f.close()