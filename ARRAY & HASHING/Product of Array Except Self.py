nums = [1, 2, 3, 4]
prefix = 1
suffix = 1
ans = [1] * len(nums)
for i in range(1, len(nums)):
   ans[i] = nums[i-1]* ans[i-1]

for j in range(len(nums)-1,-1,-1):
   ans[j] *= suffix
   suffix *= nums[j]



print(ans)
