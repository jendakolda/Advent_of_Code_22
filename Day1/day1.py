with open('input1.txt', 'r') as source:
    data = source.read().split('\n\n')

first_n_elves = 3
top_n = [0]
for elf in data:
    elf = sum(int(cal) for cal in elf.split('\n'))
    if any(elf > i for i in top_n):
        top_n.append(elf)
        top_n.sort(reverse=True)
        if len(top_n) > first_n_elves:
            top_n.pop()
print(sum(top_n))

