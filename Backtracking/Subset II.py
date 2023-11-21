def anssubsetswithrepetition():
   a = [1, 2, 3, 2]
   a.sort()
   ans = []
   tempans = []
   i = 0

   def subset(i, ans, tempans, a):

      # INCLUDE ELEMENT AND PROCESS
      if (i >= len(a)):
         ans.append(tempans.copy())
         return
      tempans.append(a[i])

      subset(i + 1, ans, tempans, a)
      r = len(a) - 1
      # EXCLUDE ELEMENT AND PROCESS
      tempans.pop()

      # CHECK IF IT IS A REPEATED ELEMENT
      # IMP FIRST CHECK INDEX AND INDEX ELEMENT EQUALS NEXT INDEX ELEMENT
      while (i + 1 < len(a) and a[i] == a[i + 1]):
         i = i + 1

      subset(i + 1, ans, tempans, a)

   subset(i, ans, tempans, a)
   print(ans)


print(anssubsetswithoutrepetition())

print(anssubsetswithrepetition())

