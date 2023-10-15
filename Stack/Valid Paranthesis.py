# def parenthesis():
#    b = "()[]{})"
#    l = len(b)
#    s=[]
#    for i in b:
#       if(i in '{[('):
#          s.append(i)
#       elif (i == '}'):
#          if (len(s) != 0):
#             if (s[-1] == '{'):
#                s.pop()
#             else:
#                return False
#       elif (i == ']'):
#          if (len(s) != 0):
#             if (s[-1] == '['):
#                s.pop()
#             else:
#                return False
#       elif (i == ')'):
#          if (len(s) != 0):
#             if (s[-1] == '('):
#                s.pop()
#             else:
#                return False
#          else:
#             return False
#    if(len(s) == 0):
#       return True
#
#
#
#
# print(parenthesis())
#


def parenthesis():
   b = "()[]{}"
   ma ={'{':'}','[':']','(':')'}
   s=[]
   for c in s:
      if(c not in ma):
         s.append()
      if c not in s or s[-1] != ma[c]:
         return False
      s.pop()
   return not s



print(parenthesis())