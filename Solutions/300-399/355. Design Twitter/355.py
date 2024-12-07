import heapq
from typing import List

class User:
    def __init__(self, userId: int):
        self.id = userId
        self.tweets = []
        self.following = set()
        self.following.add(userId)

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.users:
            self.users[userId] = User(userId)
        self.users[userId].tweets.append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        timeline = []
        if userId not in self.users:
            return []
        for following in self.users[userId].following:
            for time, tweet in self.users[following].tweets:
                heapq.heappush(timeline, (-time, tweet))
        newsFeed = []
        while len(newsFeed) < 10 and timeline:
            newsFeed.append(heapq.heappop(timeline)[1])
        
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)    
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        if followeeId not in self.users[followerId].following:
            return 
        self.users[followerId].following.remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)