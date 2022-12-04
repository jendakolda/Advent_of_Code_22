counter_A, counter_B = 0, 0
with open('input4.txt', 'r') as source:
    for line in source.read().splitlines():
        [(min1, max1), (min2, max2)] = [tuple(int(j) for j in i.split('-')) for i in line.split(',')]
        if (min1 <= min2 and max2 <= max1) or (min2 <= min1 and max1 <= max2):
            counter_A += 1
        if (min2 <= max1 <= max2) or (min1 <= max2 <= max1):
            counter_B += 1
print(f'Part A: {counter_A}, Part B: {counter_B}')
