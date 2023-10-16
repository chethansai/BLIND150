def generate():
   n =3
   s =[]
   res=[]

   def backtrack(o,c):

      if(o==c==n):
         res.append("".join(s))
         return
      if(o<n):
         s.append('(')
         backtrack(o+1,c)
         s.pop()


      if(o>c):
         s.append(')')
         backtrack(o, c +1)
         s.pop()

   backtrack(0,0)
   print(res)
generate()

