import numpy as np
with open('input8.txt', 'r') as source:
    forrest = np.array([[int(j) for j in i] for i in source.read().splitlines()])
directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
radky, sloupce = forrest.shape
visible = 2 * radky + 2 * (sloupce - 2)
max_scenic_score = 0
print(f'Forrest {forrest[100:100]}')
for radek in range(1, radky - 1):
    for sloupec in range(1, sloupce - 1):
        scenic_score = 0
        comparison = (
            max(forrest[radek, :sloupec]),
            max(forrest[radek, sloupec+1:]),
            max(forrest[:radek, sloupec]),
            max(forrest[radek+1:, sloupec]),
        )
        visible += any(maximum < forrest[radek, sloupec] for maximum in comparison)

        for direction in directions:
            coords = [radek, sloupec]
            lower = True
            while lower:
                coords[:] += direction[:]
                print(f)
                # if
                # scenic_score += forrest[coords] <= forrest[radek, sloupec]

print(f'Part A: {visible}, Part B: {None}')
