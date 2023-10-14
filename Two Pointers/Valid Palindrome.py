def isalphanum(l):
   return(ord('A') <= ord(l) <= ord('Z') or
          ord('0') <= ord(l) <= ord('9') or
          ord('a') <= ord(l) <= ord('z') )
def palindrome():
   s = "A man, a plan, a canal: Panama"
   l = 0
   r = len(s) - 1
   while(l<r):
      while(l < r and not isalphanum(s[l]) ):
         l += 1
      while (l < r and not isalphanum(s[r])):
         r -= 1
      if(s[r].lower() != s[l].lower()):
         return False
      l += 1
      r -= 1
   return True




palindrome()
print(isalphanum("b"))

