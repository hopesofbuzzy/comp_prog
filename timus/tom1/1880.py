nums = []
for i in range(3):
    n = int(input())
    nums.append(set(map(int, input().split()[:n])))
print(len(nums[0] & nums[1] & nums[2]))