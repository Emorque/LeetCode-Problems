from typing import List
import heapq

class User:
    def __init__(self, id):
        self.id = id
        self.tweets = []
        self.following = set()

class Twitter:

    def __init__(self):
        self.twitter = {}
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timeStamp += 1
        if userId not in self.twitter:
            self.twitter[userId] = User(userId)
        heapq.heappush(self.twitter[userId].tweets, (self.timeStamp * -1, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:     
        if userId not in self.twitter:
            self.twitter[userId] = User(userId)

        feed = []
        for tweet in self.twitter[userId].tweets:
            heapq.heappush(feed, tweet)

        for follow in self.twitter[userId].following:
            if follow not in self.twitter:
                continue
            for tweet in self.twitter[follow].tweets:
                heapq.heappush(feed, tweet)
        output = []
        for i in range(10):
            if not feed:
                break
            output.append(heapq.heappop(feed)[1])
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.twitter:
            self.twitter[followerId] = User(followerId)
        if followerId == followeeId or followerId not in self.twitter:
            return
        self.twitter[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.twitter:
            self.twitter[followerId] = User(followerId)

        if followerId == followeeId:
            return

        if followeeId in self.twitter[followerId].following:
            self.twitter[followerId].following.remove(followeeId)
        return

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)