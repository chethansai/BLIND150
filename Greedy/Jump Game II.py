def jump(nums):

   ans = 0

   l = 0
   r = 0

   while r < len(nums) -1:
      farthest = 0
      for i in range(l, r + 1):
         farthest = max(farthest, l + nums[i])
      l = r + 1
      r = farthest
      ans = ans + 1
   print(ans)



def codejudge():
   nums = [2, 3, 1, 1, 4]
   jump(nums)
codejudge()