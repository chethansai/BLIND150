# most to be frequenctly used is maximum
# most to be preciously used is minimum

# order by most available
# pop one each at a time  - # accomodate for frequently # its process contained object sent from heap to queue
   # do frequently ones - # accomdate if this has to be prioritized to be popped first # its process contained sent from queue to heap
import heapq


def task(n, l):
   q = []
   d = {}
   for i in l:
      if i not in d:
         d[i] = 0
      d[i] = d[i] + 1
   t = []
   for a in d.values():

      heapq.heappush(t, a * -1)
   print(l)
   print(q)
   print(d)
   print(t)
   time = 0
   print(time)
   while q or t:
      time += 1
      if t:
         temp = heapq.heappop(t)
         temp = temp + 1
         if(temp <0):

            q.append([temp, time + n])
            print(t)
      if q:
         if( q[0][1] == time):
            temp2 = q.pop(0)
            temp3 = temp2[0]
            heapq.heappush(t, temp3)
            print(q)
   print(time)




def codejudge():
   n = 2
   l = ["A","A","A","B","B","B"]
   print(task(n, l))
codejudge()
