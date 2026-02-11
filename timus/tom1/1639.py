a, b = map(int, input().split())
print("[:=[first]" if a*b % 2 == 0 else "[second]=:]")