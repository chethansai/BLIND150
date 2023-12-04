import heapq


def klargest(l, k):
   a =[]
   for i in l:
      heapq.heappush(a,i * (-1))
   while(k>=0):
      heapq.heappop(a)
      k = k - 1
   return (heapq.heappop(a) * (-1))

def codejudge():
   l = [3,2,1,5,6,4]
   # 1 2 3 4 5 6
   k = 2
   print(klargest(l, k))
codejudge()