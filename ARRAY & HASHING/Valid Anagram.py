# s = "car"
# t = "rat"
# if(len(s) ==  len(t)):
#    for i in s:
#       if(i not in t):
#          print("not an anagramm")
#          break
#    else:
#       print("Anagram")
#
# else:
#    print("not an anagram")
def anagram():
   s = "car"
   t = "rat"
   if(len(s) !=  len(t)):
      return False
   print("Ds")
   ss,tt={},{}
   for i in range(len(s)):
      ss[s[i]] = 1 + ss.get(s[i],0)
      tt[t[i]] = 1 + tt.get(t[i], 0)
      print(i)
   print(ss,tt)
   return ss == tt

print(anagram())