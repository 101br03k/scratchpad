from functools import cmp_to_key
from operator import eq, ne

rules, updates = open('input').read().split('\n\n')
cmp = cmp_to_key(lambda x,y: 1-2*(f'{x}|{y}' in rules))

for op in eq, ne: 
    ans = 0
    for line in updates.split():
        orig = line.split(',')
        good = sorted(orig, key=cmp)
        if op(orig, good):
            ans += int(good[len(good)//2])
    print(ans)