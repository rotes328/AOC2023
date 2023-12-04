total = 0
with open('data.txt', 'r', encoding='UTF-8') as data:
    for line in data.read().splitlines():
        winners = set(line.split(':')[1].split('|')[0].split())
        picks = set(line.split(':')[1].split('|')[1].split())
        total += 2 ** (len(winners & picks) - 1) if (winners & picks) else 0
print(total)
