
from typing import List
class Solution:
   def maxProduct(self, nums: List[int]) -> int:
      mi = 1
      ma = 1
      res = 0
      for i in nums:
         if(i == 0):
            mi,ma =1,1
         temp = i * ma
         ma = max(i * ma, i * mi, i)
         mi = min(temp, i * mi, i)
         res = max(res,ma)
      print(res)


s = Solution()
print(s.maxProduct([2,3,-2,4]))
