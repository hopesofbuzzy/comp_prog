import sys
n = list(map(int, sys.stdin.read().split()))
print(n[0]-n[1]*n[2] if n[1]>1 and n[2]>1 else n[0]-n[1]-n[2])