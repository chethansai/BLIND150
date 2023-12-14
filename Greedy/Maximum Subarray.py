
def kadane(a):
   l = 0
   r = 0
   a_l = 0
   a_r = 0
   ans = a[0]
   c = a[0]
   for r in range(0, len(a)):
      c = c + a[r]
      if(c < 0):
         c = 0
         l = r

      if(ans< c):
         ans = c
         a_l = l
         a_r = r
   print(ans, a_l, a_r)
   print(ans, a[a_l:a_r+1])


def codejudge():
   a = [-2,1,-3,4,-1,2,1,-5,4]
   kadane(a)
codejudge()