# largest sum
# 1 2 3 4 5 6 .
# A mid point. LEFT . RIGHT. 3 is negative enough to make (1+2) negative.
                                          # So 4 - 6 greater than 1 - 6

# so might as well choose 4 - 6
# so might as well choose 4 - 6 largest [or (4-5), (5-6)]
# but it is only when 4 - 6
   # can be a positive  :-: current = 0
      # can be an answer positive :-: ans = current

                                          # capture largest positive 1 - 3  = answer

def kadane(a):
   ans = a[0]
   c = 0
   for i in a:
      c = c + i
      if(c > ans):
         ans = c
      if(c < 0):
         c = 0
   print(ans)

def kadanesliding(a):

   ans = a[0]
   l = 0
   r = 0
   a_l = 0
   a_r = 0
   c = 0

   for r in range(len(a)):
      c = c + a[r]
      if(c < 0):
         c = 0
         l = r
      if(ans < c):
         ans = c
         a_l = l
         a_r = r
   print(ans,a_l, a_r)




def codejudge():
   a = [2, -1, 3, 1, -7, 4]

   kadane(a)
   kadanesliding(a)

codejudge()