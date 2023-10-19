# def per():
#    s1 = "ab"
#    s2 = "eidbaooo"
#    ds1 = dict()
#    ds2 = dict()
#    for i in range(ord('a'),ord('z')+1):
#       print(chr(i))
#       ds1[chr(i)]=0
#       ds2[chr(i)] = 0
#    # print(ds1,ds2)
#    for i in range(0,len(s1)):
#        ds1[s1[i]] = ds1[s1[i]] + 1
#    l = 0
#    r = len(s2)
#
#    while(l<len(s2)-len(s1)):
#       ds3 =ds2.copy()
#       for i in range(l,len(s1)+1):
#          ds3[s2[i]] = ds3[s2[i]] + 1
#          if(ds1==ds3):
#             return True
#       l = l+1
#
#
# per()
def anagram(s,t):

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
def per():


   s1 = "ab"
   s2 = "eidbaooo"

   for i in range(0,len(s2)-len(s1)+1):
      c=s2[i:i+len(s1)]
      if(anagram(s1,c)):

         return True



per()