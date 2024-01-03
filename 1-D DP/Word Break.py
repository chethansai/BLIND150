
from typing import List
class Solution:
   def wordBreak(self, s: str, wordDict: List[str]) -> bool:

      dp = [False] * (len(s) + 1)
      dp[len(s)] = True

      for i in range(len(s) - 1, -1, -1):
         for j in wordDict:
            if(i + len(j) <= len(s) and s[i : i + len(j)] == j):
               dp[i] = dp[i + len(j)]
      print(dp[0])



s = Solution()
print(s.wordBreak("applepenapple",["apple","pen"]))
