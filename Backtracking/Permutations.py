
def answer1():
   ans = []
   n = [1, 2, 3]

   def backtrack(n, path):
      if len(path)==2:
         ans.append(path.copy())
         return

      for i in range(len(n)):
         path.append(n[i])
         changed_n = n[:i] + n[i + 1:]
         backtrack(changed_n, path)
         path.pop()

   backtrack(n, [])
   return ans


print(answer1())
