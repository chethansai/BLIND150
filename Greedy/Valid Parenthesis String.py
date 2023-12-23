def parenthesis(s):
   print(s)
   l_min = 0
   l_max = 0

   for i in s:
      print(i)
      if(i == '('):
         l_min = l_min + 1
         l_max = l_max + 1
      if(i == '*'):
         l_max = l_max + 1
         l_min = l_min - 1
      if(i == ')'):
         l_min = l_min - 1
         l_max = l_max - 1
      if(l_min < 0):
         l_min = 0
      if(l_max < 0):
         return False

   if(l_min == 0):
      return True
   else:
      return False

def codejudge():
   s = "(*)"
   parenthesis(s)
codejudge()