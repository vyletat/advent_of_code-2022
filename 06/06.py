f = open("input.txt", "r")

signal = f.readline().strip()
# make signal as string
signal = ''.join(map(str, signal))

same_char = 14
# iterate over signal and pick 4 elements
for i in range(len(signal) - (same_char - 1)):
    sequence = signal[i:i + same_char]
    # make sequence as character list
    sequence_list = list(sequence)
    # find same elements in sequence
    same_elements = [x for x in sequence_list if sequence_list.count(x) > 1]
    # if there are different elements in sequence
    if len(same_elements) == 0:
        print(sequence)
        print(signal.index(sequence) + same_char)
        break






