
# REMOVE GREATER THAN REMAINING AMOUNT COIN AMOUNTS
# VALUE OF FIT AMOUNT UNIVERSE- REMOVE FROM REMAINING. CALCULATE TOTAL


from typing import List
class Solution:
   def coinChange(self, coins: List[int], amount: int) -> int:
      dp = [amount + 1] * (amount + 1)
      dp[0] = 0
      for i in range(amount + 1):
         for c in coins:
            if(i - c >= 0):
               dp[i] = min(dp[i], 1 + dp[i - c])
      return dp[amount]

s = Solution()
print(s.coinChange([1,2,5],11))

