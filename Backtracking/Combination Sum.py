
def answer():
   ans =[]
   n =7
   def combinationk2n(i, tempans, ans, n, summ):
      if(summ == 7):
         ans.append(tempans.copy())
         return
      if(summ > 7 or i>=n):
         return
      tempans.append(i)

      combinationk2n(i, tempans, ans, n,  summ+i)
      tempans.pop()

      combinationk2n(i + 1, tempans, ans, n,  summ)

   combinationk2n(1, [], ans, n,  0)
   return (ans)


def answer1():
   ans = []
   n = 5
   k = 2
   i = 1
   tempans = []


   def combinationk2n(i, tempans, ans, n, k):
      if(len(tempans) == k):
         ans.append(tempans.copy())
         return
      if(i>n):
         return





      for i in range(i,n+1):
         tempans.append(i)


         combinationk2n(i+1, tempans, ans, n, k)
         tempans.pop()


   combinationk2n(i, tempans, ans, n, k)
   return (ans)


print(answer())

