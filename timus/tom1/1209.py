def f(x):
    i = 1
    d = 1
    while i <= x:
        yield i
        i += d
        d += 1



n = int(input())
nums = [int(input()) for _ in range(n)]
r = ["0" for i in range(n)]
for i in f(max(nums)):
    if i in nums:
        r[nums.index(i)] = "1"
print(" ".join(r))
