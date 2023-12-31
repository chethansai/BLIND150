def palindrome(p):
   ans = []
   for i in range(len(p)):


      s = i
      e = i
      while(s >= 0 and e <= len(p) -1 and p[s] == p[e]):
         ans.append(p[s:e+1])
         s = s-1
         e = e+1

      s = i
      e = i + 1
      while (s >= 0 and e < len(p) -1 and p[s] == p[e]):
         ans.append(p[s:e + 1])
         s = s - 1
         e = e + 1
   print(ans)


def codejudge():
   p = 'racecar'
   palindrome(p)

codejudge()