
def decode(s):

      #do not know next
      #do not know next next

      #why sum and not either one
      # 121 222112221222
      # 1
      # 12

      #think 1 and 3 combinations - 21 222112221222
      #think 12 and 4 combinations - 1 222112221222
      #decsion to be made at 1
      # (1) - 3
         # () - 1st[23]                = (1) [23]   =123
         # () - 2nd[24]                = (1) [24]   =124
         # () - 3rd[25]                = (1) [25]   =125
      # (12) - 4
         # () - 1st[11]                = (12) [11]  =1211
         # () - 2nd[12]                = (12) [12]  =1212
         # () - 3rd[13]                = (12) [13]  =1213
         # () - 4th[14]                = (12) [14]  =1214

      #HENCE FOR ALL POSSIBILITES SUM (3 +4) =7

   dp = {len(s): 1}



   def dfs(i):
      if i in dp:
         return dp[i]
      if s[i] == "0":
         return 0


      res = dfs(i + 1)
      if i + 1 < len(s) and (
            s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
      ):
         res += dfs(i + 2)
      dp[i] = res
      return res


   return dfs(0)


def codejudge():
   s = "226"
   return (decode(s))

print(codejudge())