from string import ascii_letters
priority_A, priority_B = 0, 0
with open('input3.txt', 'r') as source:
    data = source.read().splitlines()
    # Part A
    for line in data:
        for letter in line[:len(line)//2:]:
            if letter in line[len(line)//2::]:
                priority_A += ascii_letters.index(letter) + 1
                break
    # Part B
    for i, j, k in zip(data[::3], data[1::3], data[2::3]):
        for letter in i:
            if letter in j and letter in k:
                priority_B += ascii_letters.index(letter) + 1
                break
print(f'Part A: {priority_A}, Part B: {priority_B}')
