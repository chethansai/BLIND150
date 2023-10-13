nums = [1,2,3,1]

for i in range(0,len(nums)):
   # print(nums[i])
   if(nums[i] in nums):
      print("CONTAINS DUPLICATE")
      break
else:
   print("CONTAINS DUPLICATE")