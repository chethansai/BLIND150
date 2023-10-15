def notation():
   s=[]
   t = ["4","13","5","/","+"]
   a = 0
   for i in t:
      if(i == '+'):
         a = int(s.pop()) + int(s.pop())
         s.append(a)
      elif(i == '-'):
         a = int(s.pop()) - int(s.pop())
         s.append(a)
      elif(i == '*'):
         a = int(s.pop()) * int(s.pop())
         s.append(a)
      elif(i == '/'):
         a1 = int(s.pop())
         a2 = int(s.pop())
         a =  a2 /a1
         s.append(a)
      else:
         s.append(int(i))
      print(s[-1])

   print(s)



notation()