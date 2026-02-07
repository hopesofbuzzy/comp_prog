k, n = map(int, input().split())
a = list(map(int, input().split()))
r = 0
for ai in a:
    r += ai
    r -= k
    r = 0 if r < 0 else r
print(r)