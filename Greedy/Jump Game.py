def jump(nums):

   goal = len(nums) - 1

   for i in range(len(nums) - 1, -1, -1):
      # print(i)
      print(nums[i])
      if ((i + nums[i])>= goal):
         goal = i
   if goal == 0:
      return True
   else:
      return False
def codejudge():
   nums = [2,3,1,1,4]
   return (jump(nums))
print(codejudge())