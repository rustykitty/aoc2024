import sys
import itertools
from collections import deque
data = [x.split(': ') for x in sys.stdin.read().rstrip().split('\n')]

res = 0

# def product(it, times):
#     it = list(it)
#     counter = 0
#     for _ in range(len(it) ** times):
#         x = deque(maxlen=times)
#         y = counter
#         for _ in range(times):
#             x.appendleft(it[y % len(it)])
#             y //= len(it)
#         yield tuple(x)
#         counter += 1

def repr_lambda(f):
    if f == funcs[0]:
        return "add"
    elif f == funcs[1]:
        return "mul"
    else:
        return "None"

funcs = [lambda x, y: x + y, lambda x, y: x * y]

for i in data:
    a, b = i
    a = int(a)
    b = tuple(int(x) for x in b.split(' '))
    for x in itertools.product(funcs, repeat=len(b) - 1):
        # print([repr_lambda(f) for f in x])
        r = b[0]
        for j in range(len(b) - 1):
            r = x[j](r, b[j + 1])
        # print(a, r)
        if a == r:
            res += r
            break

print(res)