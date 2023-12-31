def house(nums,n):
   h1,h2 = 0,0
   for i in nums:
      temp = max(h1 + i, h2)
      h1 = h2
      h2 = temp
   print(h2)
def codejudge():
   nums = [1, 2, 3, 1]
   n = 4
   house(nums,n)
codejudge()