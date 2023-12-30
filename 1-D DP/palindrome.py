#palindromebruteforce
def bf(w):
   e = len(w) -1
   s = 0
   while(e >= s ):
      if(w[s] != w[e]):
         return False
      e = e - 1
      s = s + 1
   return True

#longestpalindromedp
def dp(w):
   ans = 0
   ans_word =''
   for i in range(len(w)):

      #odd
      s = i
      e = i
      while(s >= 0 and e < len(w) and w[s] == w[e] ):
         if(ans < e - s):
            ans = e - s + 1
            ans_word = w[s:e+1]
         s = s - 1
         e = e + 1
      #EVEN
      s = i
      e = i + 1
      while(s >= 0 and e < len(w) and w[s] == w[e] ):
         if(ans < e - s):
            ans = e - s + 1
            ans_word = w[s:e+1]
         s = s - 1
         e = e + 1
   print(ans)
   print(ans_word)



def codejudge():

   w = "raceecar"
# palindromebruteforce
#    return (bf(w))

#longestpalindromedp
   dp(w)
print(codejudge())