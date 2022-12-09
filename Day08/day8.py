import numpy as np
with open('input8.txt', 'r') as source:
    forrest = np.array([[int(j) for j in i] for i in source.read().splitlines()])
directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
radky, sloupce = forrest.shape
visible = 2 * radky + 2 * (sloupce - 2)
max_tree_score = 0
for radek in range(1, radky - 1):
    for sloupec in range(1, sloupce - 1):
        # Part A
        comparison = (
            max(forrest[radek, :sloupec]),
            max(forrest[radek, sloupec+1:]),
            max(forrest[:radek, sloupec]),
            max(forrest[radek+1:, sloupec]),
        )
        visible += any(maximum < forrest[radek, sloupec] for maximum in comparison)
        # Part B
        tree_score = 1
        for direction in directions:
            dir_score = 0
            coords = [radek, sloupec]
            while True:
                row, col = coords = [coord + direct for coord, direct in zip(coords, direction)]
                if row not in range(radky) or col not in range(sloupce):
                    break
                elif forrest[row, col] <= forrest[radek, sloupec]:
                    dir_score += 1
                    if forrest[row, col] == forrest[radek, sloupec]:
                        break
                else:
                    break
            tree_score *= dir_score
        max_tree_score = max(max_tree_score, tree_score)
print(f'Part A: {visible}, Part B: {max_tree_score}')
