

def answer():
   ans = []
   s = "abc"
   k = 2
   i = 0
   n=len(s)
   print(n)
   tempans = []


   def combinationk2n(i, tempans, ans, n, k):
      if(i<=n):
         print(tempans)
         ans.append(tempans.copy())

      if(i>=n):
         return




      tempans.append(s[i])



      combinationk2n(i+1, tempans, ans, n, k)
      tempans.pop()
      combinationk2n(i+1, tempans, ans, n, k)

   combinationk2n(i, tempans, ans, n, k)
   return (ans)


def answer1():
   ans = []
   s = "aac"
   k = 2
   i = 0
   n=len(s)
   print(n)
   tempans = []

   def ispalindrome(s):
      i,j = 0, len(s) -1
      while(i<=j):
         if(s[i] == s[j]):
            i = i + 1
         else:
            return False
      return True

   def combinationk2n(i, tempans, ans, n, k):

      if(i>=n):
         ans.append(tempans.copy())
         return


      for j in range(i,n):
         print(ispalindrome(s[i:j+1]))
         if(ispalindrome(s[i:j+1])):

            tempans.append(s[i:j+1])


            combinationk2n(j+1, tempans, ans, n, k)
            tempans.pop()


   combinationk2n(i, tempans, ans, n, k)
   return (ans)

#
# print(answer())

print(answer1())

