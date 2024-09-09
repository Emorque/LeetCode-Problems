1. Share questions you would ask to help understand the question:
- Can a user follow themselves?
- Are tweets made have ascending ids?
- Is there no limit to how many people a person can follow?
- Can a person follow someone who hasn't been called yet?
- Is it okay to discard oldest tweets if a user tweets more than 10 times?
- Can someone unfollow from someone they haven't followed or themselves?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hashmap (Likely)
- Heap (Likely)

3. Write out in plain English what you want to do: 
- Looking that this question, the concept of userIds reminds me of a database, so a hashmap should be useful here. 
- At the idea of only returning the 10 most recent tweets, meanings that some order of ordering should be maintined, meaning a heap could be useful. 
- At initailization a hashmap should be initialized 
- The key will be the usersIds
    - important data to remember are tweets made by this user, who they are following
    - The tweets can be contained within a heap. Therefore, a general timestamp int will be used to track when tweets are made, and this int will be what the heap uses to order the tweet ids
    - The followers can be a set

4. Translate each sub-problem into pseudocode:
- init: 
    - twitter = {}
    - timestamp = 0

- postTweet: 
    - timestamp += 1
    - twitter[userId] = [][]
    - heapq.heappush(twitter[userId][0], (timestamp, tweetId)

- getNewsFeed: 
    - if len(twitter[userid][1]) == 0:
        - return twitter[userId][0]
    - output = twitter[userId][0]
    - for follow in twitter[userId][1]:
        - for tweet in twitter[follow][1]
            - heapq.heappush(output, tweet)
    - return output

- follow: 
    - if ids ==: return 
    - twitter[userId][1].add(followeerID)

- unfollow: 
    - if ids ==: return 
    - twitter[userId][1].remove(followeerID)

5. Translate the pseudocode into Python and share your final answer:
  <!-- class User:
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
            return -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that there is a there is a hashmap and set used in the user and twitter class to allow for efficient storage and lookups
- One weak area is that this is certainly a more complicated approach
    - I made my own user class to clearly know what a user has, tweets and their following list
    - And since, I made my Twitter work by having the newsFeed function go through each person the user follows
        - This is a tradeoff that I think made more since, as the benefit is that posting tweets is very fast
        - The opposite of this approach would have been to have posting tweets take a long time, iterating through the list of every person that follows this user
            - This also gets complicated when a user can be unfollowed
            - The benefit is that getting newsFeeds gets much quicker
- I actually liked this question, and it made me think of the tradeoffs of how certain approaches work. I'll definetly write down revisitng this question later, and see how different my approach will be. 