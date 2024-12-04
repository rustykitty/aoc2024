import sys

safe_reports = 0

while (line := sys.stdin.readline()):
    if (line == '\n'): break
    report = [int(level) for level in line[:-1].split(' ')]
    # print(report)
    how_safe = 0
    up = []
    for i in range(len(report) - 1):
        if not ((3 >= abs(report[i] - report[i + 1]) >= 1)):
            how_safe += 1
        if report[i] - report[i + 1] > 0:
            up.append(True)
        else:
            up.append(False)
    up_count = up.count(True)
    down_count = up.count(False)
    if up_count == 1 or down_count == 1:
        how_safe += 1
    if how_safe < 2: 
        safe_reports += 1

print(safe_reports)
