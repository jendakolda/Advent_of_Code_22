def get_nonrepeating_sequence(string, length):
    for i, letter in enumerate(string):
        if len(set(string[i - length:i])) == length:
            return i


with open('input6.txt', 'r') as source:
    data = source.read()
print(f'Part A: {get_nonrepeating_sequence(data, 4)}, Part B: {get_nonrepeating_sequence(data, 14)}')
