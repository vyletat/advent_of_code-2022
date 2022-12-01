file_input = open("input.txt", "r")
elf = []

sum = 0
# read input and if there is number add it to total and if not read next line and add total to elf
for line in file_input:
    line = line.strip()
    if line.isdigit():
        sum += int(line)
    else:
        elf.append(sum)
        sum = 0
        continue
elf.append(sum)
print(max(elf))

# find 3 max numbers in elf and sum them
elf.sort(reverse=True)
print(elf[0] + elf[1] + elf[2])