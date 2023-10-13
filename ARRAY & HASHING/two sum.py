def twosum():
   print("gf")
   nums = [2,7,11,15]
   target = 9
   for i in range(len(nums)):
      if((target - nums[i]) in nums):
         print(i,nums.index(target-nums[i]))
         return
twosum()