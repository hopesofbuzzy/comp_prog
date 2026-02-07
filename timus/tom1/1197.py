n = int(input())

for _ in range(n):
    pos = input()
    r = 8
    i = 2
    j = 2
    if pos[0] in "abgh":
        r -= 2
        i -= 1
        if pos[0] in "ah":
            r -= 2
            j -= 1
    if pos[1] in "1278":
        r -= j
        if pos[1] in "18":
            r -= i
    print(r)
# Использовал некоторые эвристики, развив базовую идею
# О том, что по краям убираем по две клетки