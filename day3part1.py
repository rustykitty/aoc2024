import re
import sys
expr = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)")

data = sys.stdin.read()

res = 0

enabled = True

for match in expr.finditer(data):
    print(data[match.start():match.end()])
    if data[match.start():match.end()] == "don't()":
        enabled = False
        continue
    elif data[match.start():match.end()] == "do()":
        enabled = True
        continue
    if enabled:
        res += int(match.group(1)) * int(match.group(2))

print(res)
