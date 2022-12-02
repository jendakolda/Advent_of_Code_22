def get_result(line):
    '''Funkce vezme hodnoty na radku, a vrati pocet bodu podle toho, co oba hraci zahrali'''
    match line:
        case ('A Y' | 'B Z' | 'C X'):  # win
            return 6
        case ('A X' | 'B Y' | 'C Z'):  # draw
            return 3
        case ('A Z' | 'B X' | 'C Y'):  # loose
            return 0


def get_my_choice(line):
    '''Funkce vrati co mam zahrat (pocet bodu pro danou volbu), podle pozadovaneho vysledku hry'''
    match line:
        case ('A X' | 'B Z' | 'C Y'):  # scissors
            return 3
        case ('A Z' | 'B Y' | 'C X'):  # paper
            return 2
        case ('A Y' | 'B X' | 'C Z'):  # rock
            return 1


my_choice = {'X': 1, 'Y': 2, 'Z': 3}  # body podle toho, co jsem zahral
result = {'X': 0, 'Y': 3, 'Z': 6}
score_A, score_B = 0, 0
with open('input2.txt', 'r') as source:
    for line in source.read().splitlines():  # vezme celej vstup, nacte, a rozseka na radky. "for" potom prochazi jednotlive radky
        score_A += get_result(line) + my_choice[line.split(' ')[-1]]  # k celkovemu skore pripocte vysledek z noveho radku a taky body za mou volbu
        score_B += get_my_choice(line) + result[line.split(' ')[-1]]
print(f'Part A: {score_A}, Part B: {score_B}')
