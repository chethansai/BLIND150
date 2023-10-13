import collections
def longest():
   nums =[100,4,200,1,3,2]
   ans = collections.defaultdict(set)
   longest =1
   for i in range(len(nums)):
      if(nums[i]-1 not in nums):
         ans[i].add(nums[i])
   for key,value in ans.items():
      temp=0
      while(key +1 in nums ):
         print(key )
         key += 1
         temp = temp + 1
         longest = max(longest,temp)

   print("longest" )
   print(longest)






   print(ans)
longest()
