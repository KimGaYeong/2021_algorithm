import sys

a, c = [], []
a = sys.stdin.readline().split('-')

alen = len(a)
for i in a:
    if i.find('+'):
        c.append(sum(list(map(int, i.split('+')))))
    else:
        c.append(int(i))

result = c[0]
for i in range(1, alen):
    result -=c[i]

print(result)