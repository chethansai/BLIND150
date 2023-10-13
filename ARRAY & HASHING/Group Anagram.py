
# import collections
# def isAnagram(a,b):
#    res = collections.defaultdict(list)
#    count = [0] * 26
#    for i in a:
#
#       count[ord(i) - ord("a")] +=1
#
#    res[tuple(count)].append(a)
#    count = [0] * 26
#    for j in b:
#       count[ord(j) - ord("a")] +=1
#    res[tuple(count)].append(b)
#    print(res)
#
# isAnagram("ate","eat")



import collections


def groupAnagram():
   res = collections.defaultdict(list)
   strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
   for s in strs:
      count = [0] * 26
      for i in s:
         count[ord(i) - ord("a")] +=1
      res[tuple(count)].append(s)
   print(res.values())


groupAnagram()