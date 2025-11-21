import sys

lines = sys.stdin.readlines()
print('This is a line: ', lines)

for line in sys.stdin:
    print(line[:-1])