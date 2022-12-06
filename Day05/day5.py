from copy import deepcopy
from parse import *
crates_A = {}
with open('input5.txt', 'r') as source:
    layout, moves = source.read().split('\n\n')
layers = layout.split('\n')
col_nums = layers[-1].translate(' ')  # takes the last line and removes blank spoces
for column in map(int, col_nums.split()):
    crates_A[column] = []  # creates a dictionary with integers from last line as keys and empty lists as values

for num, layer in enumerate(reversed(layers[:-1])):
    l = [layer[i * 4: i * 4 + 4].strip(' []') for i in range(len(layer)//4 + 1)]
    for column, i in zip(map(int, col_nums.split()), range(len(l))):
        if l[i] != '':
            crates_A[column].append(l[i])
crates_B = deepcopy(crates_A)
for move in moves.splitlines():
    r = parse('move {how_many} from {frm} to {to}', move)
    # part A
    for i in range(int(r['how_many'])):
        crates_A[int(r['to'])].append(crates_A[int(r['frm'])].pop())
    # part B
    crates_B[int(r['to'])].extend(crates_B[int(r['frm'])][-int(r['how_many']):])
    del crates_B[int(r['frm'])][-int(r['how_many']):]
print('Part A:')
for value_A in crates_A.values():
    print(value_A[-1], end='')
print('\nPart B:')
for value_B in crates_B.values():
    print(value_B[-1], end='')
