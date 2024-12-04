import sys

safe_reports = 0

while (line := sys.stdin.readline()):
    if (line == '\n'): break
    report = [int(level) for level in line[:-1].split(' ')]
    is_safe = True
    up = []
    for i in range(len(report) - 1):
        if not (3 >= abs(report[i] - report[i + 1]) >= 1):
            is_safe = False
            break
        if (report[i] - report[i + 1]) > 0:
            up.append(True)
        else:
            up.append(False)
    is_safe = is_safe and (all((not i for i in up) if up[0] == False else up))
    if is_safe: 
        safe_reports += 1

print(safe_reports)
