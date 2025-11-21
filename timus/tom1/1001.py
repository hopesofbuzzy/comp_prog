import sys
from math import sqrt

print('\n'.join(reversed([f'{sqrt(num):.4f}' for num in map(int, sys.stdin.read().split())])))