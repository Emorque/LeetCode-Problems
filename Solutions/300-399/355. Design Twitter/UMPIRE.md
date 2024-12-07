1. List out any clarifying questions:
- Can a user follow/unfollow themselves
- Since I need to return the most recent tweets, would it be it be beneficial to have an external timer 
- Will the follow Ids in follow and unfollow all be already created users?

2. List out 1-3 data structures/algorithms that could be useful:


3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- It would be good to break this down into individual problems to find suitable strucutres
- For tweetId and userID, this looks like a great case for hashmaps, where key is userID and for now, value is a list of tweetIds theyve made
- Next comes the relationship between followers and followees
- I've thought of two different structures that could be used here, linkedLists and heaps
- with LLs, I can construct a general timeline of nodes comprised of the user's tweets. Then, if the user follows someone, I'll merge the tweets of this person's Timeline with the tweets of the person their following
- The caveat is that once unfollowed, I'd have to go through this entire LL structure to remove all nodes with that person
- With a heap, once getNewsFeed is called, I'll construct a heap by heappush all tweets of the people the current person is following
- Then if someone is no longer following person x, I just removed that person from the user's following list
- It bascially comes with do I want longer time to construct the newsfeed or longer time to deal with following/unfollowing a person

4. Assess the space/time complexity:
- Space: O(f*t) for storing the all following tweets in the timeline for getNewsFeed. The other function functions are all O(1). The 
- Time: postTweet, follow, and unfollow are all O(1)
    - getNewsFeed is O(f*tlog10) which comes from the 10 times logft is called with heappush

5. Optional - Give any ways you would improve your solution: