n = int(input())
r = 2
for _ in range(n):
    answer = input()
    r = r + 2 if answer[-4:] == "+one" else r + 1
if r == 13:
    r += 1
print(r*100)