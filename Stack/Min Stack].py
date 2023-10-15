class stack:
   def __init__(self):
      self.s  = []
      self.ms = []
   def push(self,a):
      self.s.append(a)
      self.ms.append(min(a,self.ms[-1]) if self.ms else a)

   def pop(self):
      self.s.pop()
      self.ms.pop()
   def top(self):
      return self.s[-1]

   def gmini(self):
      return self.ms[-1]

o = stack()
o.push(-2)