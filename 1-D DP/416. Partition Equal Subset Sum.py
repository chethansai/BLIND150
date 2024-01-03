
from typing import List
class Solution:
   def canPartition(self, nums: List[int]) -> bool:

      dp = set()
      dp.add(0)
      target = sum(nums) // 2

      if( sum(nums)  % 2 != 0):
         return False
      for i in range(len(nums)):
         temp_dp = set()

         for j in dp:
            temp_dp.add(j)
            temp_dp.add(nums[i] + j)
            if(nums[i] + j == target):
               return True
         dp = temp_dp
      return False


s = Solution()
print(s.canPartition([1,5,11,5]))
