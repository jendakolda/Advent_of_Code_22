with open('input1.txt', 'r') as source:
    data = source.read().split('\n\n')


def find_max_elf(data, first_n_elves):
    top_n = [0]
    for elf in data:
        elf = sum(int(cal) for cal in elf.split('\n'))
        if any(elf > i for i in top_n):
            top_n.append(elf)
            top_n.sort(reverse=True)
            if len(top_n) > first_n_elves:
                top_n.pop()
    return sum(top_n)


print(f'First part: {find_max_elf(data, 1)}')
print(f'Second part: {find_max_elf(data, 3)}')
