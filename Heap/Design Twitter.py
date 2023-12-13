
#follow
import heapq


def follow(followerId, followeeId):
   if(followerId not in users):
      users[followerId] =set()
      users[followerId].add(followerId)
   if(followeeId not in users):
      users[followeeId] =set()
      users[followeeId].add(followeeId)
   users[followerId].add(followeeId)
   #unfollow
def unfollow(followerId, followeeId):
   if(followerId not in users):
      users[followerId] =set()
      users[followerId].add(followerId)
   if(followeeId not in users):
      users[followeeId] =set()
      users[followeeId].add(followeeId)
   users[followerId].remove(followeeId)

#postTweet
def postTweet(userId, tweetId):
   if(userId not in users):
      users[userId] =set()
      users[userId].add(userId)
   if(userId not in tweets):
      tweets[userId] =list()
   global tweettime
   tweettime += 1
   tweets[userId].append([tweettime, tweetId])


#getNewsFeed
def getNewsFeed(userId):
   print(users)
   if(userId not in users):
      return False
   feedheap = []

   for u in users[userId]:
      for f in tweets[u]:

         heapq.heappush(feedheap,f)
   popcounter = 10
   while(len(feedheap)>0 and popcounter >0):
      popcounter = popcounter - 1
      print(heapq.heappop(feedheap))

def design(p, i):
   for j in range(len(p)):
      print(p[j])
      print(i[j])
      if(p[j] == 'follow'):
         follow(i[j][0], i[j][1])
      if (p[j] == 'unfollow'):
         unfollow(i[j][0], i[j][1])
      if (p[j] == 'postTweet'):
         postTweet(i[j][0], i[j][1])
      if (p[j] == 'getNewsFeed'):
         getNewsFeed(i[j][0])


def codejudge():
   p = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
   i = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
   design(p,i)
#user-tweet
tweets= dict()
tweettime = 0
#user - followers
users = dict()
codejudge()