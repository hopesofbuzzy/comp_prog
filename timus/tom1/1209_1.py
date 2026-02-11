import math


n = int(input())
r = []
for _ in range(n):
    i = int(input())
    t = -7+8*i
    r.append(str(int(int(math.sqrt(t))**2 == t)))
print(" ".join(r))