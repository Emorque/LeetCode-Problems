1. List out any clarifying questions:
- How does timestamp work with get? Does the key get that new timestamp?
- When timestamp is called with set, is it always in ascending order?

2. List out 1-3 data structures/algorithms that could be useful:
- Hashmap
- Binary Search 

3. Break down the problem into subproblems, provide psuedocode for these subproblems:
- After a small drawing, I can better visualize this structure. Because of the key-value relationship between the and its collection of values, I know a hashmap would be helpful in creating this relationship
- Then, thanks to my second question, I know that when I set times, a key's value list will always be in ascending order
- To minimize the need of checking every value, I can just use binary search to find the highest number that is less than timestamp
- I could store the values in the list as a pair: (timestamp, value)

4. Assess the space/time complexity:
- Space: O(n) where n in the number of timestamp, value pairs that I make, basically the number of set calls
- Time: O(logn) since I just take the n list from the key in the store hashmap, and perform binary search

5. Optional - Give any ways you would improve your solution:
- While this algorithm does work, there is a way to improve time complexity for some test cases, primarly those that have a get timestamp not within the range of the key. So checking something like:
- if timestamp < all_vals[0][0]:
        return ""
    if timestamp > all_vals[-1][0]:
        return  all_vals[-1][1] 
- Would be a great way of returning early and not performing binary search at all since its no longer necessary