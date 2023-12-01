import heapq


def stoneweight(s):
   sortedstones = []
   for i in s:
      heapq.heappush(sortedstones,(i * -1))

   while(len(sortedstones) > 1 ):
      s1 = heapq.heappop(sortedstones) * -1
      s2 = heapq.heappop(sortedstones) * -1

      if(s1==s2):
         continue
      elif(s1 > s2):
         new_stone = (s1 - s2) * -1
      else:
         new_stone = (s2 - s1) * -1
      heapq.heappush(sortedstones, new_stone)
   return (heapq.heappop(sortedstones) * -1)

def codejudge():
   s = [2, 7, 4, 1, 8, 1]

   #maxheap
   print(stoneweight(s))

codejudge()
