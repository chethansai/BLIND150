import collections
class kp:
   def __init__(self):
      self.d=collections.defaultdict(list)



   def set(self, key, value, timestamp):
      self.d[key].append([value,timestamp])


   def get(self,key, timestamp):
      i=0
      j=len(self.d[key] )-1
      ans = None
      while(i<=j):
         m = (i + j)//2
         if(self.d[key][m][1]==timestamp):
            return self.d[key][m][0]
         elif(self.d[key][m[1]]>timestamp):
            i = m + 1
         else:
            j =m - 1
      return None



a = kp()
a.set("foo", "bar", 1)
print(a.get("foo",1))
