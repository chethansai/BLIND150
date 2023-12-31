def house(nums,n):

   return max(househelper(nums[1:],n-1),nums[0],househelper(nums[:-1],n-1))
def househelper(nums,n):
   h1,h2 = 0,0
   for i in nums:
      temp = max(h1 + i, h2)
      h1 = h2
      h2 = temp
   return h2
def codejudge():
   nums = [2,3,2]
   n = 4
   return (house(nums,n))
print(codejudge())