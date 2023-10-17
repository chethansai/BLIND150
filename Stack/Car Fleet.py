# def fleet():
#    t = 10
#    p = [6, 8, 2, 12, 4]
#    s = [1, 3, 4, 2, 2]
#    print(p)
#    print(s)
#    p,s=zip(*sorted(zip(p,s)))
#
#    print(p)
#    print(s)
#    p=list(p)
#    s=list(s)
#    print(p)
#    print(s)
#    i=0
#    c=0
#    ans=0
#    i = len(p) -1
#    a=t
#    set = True
#    setS = s[len(s)-1]
#    setP = p[len(p)-1]
#
#    while(len(s) >0 ):
#       p[i] = p[i] + s[i]
#       if(i<0):
#          print('f')
#          i = len(s) -1
#          setP = p[i]
#          setS = s[i]
#       print("p",p)
#       print("s",s)
#       print("i",i)
#       print("p[i]",p[i])
#       print("s[i]",s[i])
#       print('ans', ans)
#       print("t=",t)
#       print('set=',set)
#       if(p[i]>=t  ):
#          print("sdf")
#          if(set):
#             ans +=1
#             print('ans=',ans)
#             set = False
#          p.pop()
#          s.pop()
#
#
#       elif(p[i]>=setP):
#          s[i] =  setS
#          p[i] =  setP
#
#       else:
#          setP = p[i]
#          setS = s[i]
#
#          set = True
#       i -= 1
#
#
#
#
#
#    print(ans)
#
#
# fleet()

def fleet():


   t = 10
   p = [6, 8, 2, 12, 4]
   s = [1, 3, 4, 2, 2]
   p,s = zip(*sorted(zip(p,s)))
   p =list(p)
   s =list(s)
   stack =[]
   for i in range(0,len(s)):
      time = (t-p[i])/s[i]
      stack.append(time)
      if(len(stack) >2 and stack[-1] <stack[-2]):
         stack.pop()
   print(len(stack))


fleet()