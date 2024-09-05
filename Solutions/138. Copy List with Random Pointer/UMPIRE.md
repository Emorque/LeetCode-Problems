1. Share questions you would ask to help understand the question:
- Can the LL be empty?
- Can node's random value be to a node that does not exist?
- Are the node values are unique?

- I was stumped on how to approach the index part, but looking at the node class, random is a node. From the question, and examples, it looked like random would be an int, so can I just treat random like next?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- Hashmap 

3. Write out in plain English what you want to do: 
- After reading the problem and understanding at is meant by deep-copy, the first thought that came to my head, is that a hashmap can be made from the original list 
- This hashmap will act somewhat like a graph, where it holds the relationships (.next, .random)
- At first, I was confused how I could deal with a node when it's random value is set to a future node, but with a constuctured hashamp having the relationships, this can be dealt with
- So, one iteration will go through the LL, populating the hashmap. The node in the orignial list will be the key, and the copy will be the value. I thought of maybe changing the data stored, becuase node's can get large at the start, but I am not how I could approach that optimization, if even feasible 
- Then, the LL will be iterated again, this time, grabbing the current copy node. Then, just set the .next and .random node values to the matching nodes in the hashmap

4. Translate each sub-problem into pseudocode:
- Initialize a hashmap 
- curr = head
- while curr:
  - hashmap[curr] = Node(curr.val)
  - curr++ 

- curr = head
- while curr:
  - copyNode = hashmap[curr]
  - copyNode.next = hashmap[curr.next]
  - copyNode.random = hashmap[curr.random]

- return hashmap[head]

5. Translate the pseudocode into Python and share your final answer:
  <!-- class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}

        curr = head
        while curr: 
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        hashmap[None] = None
    
        curr = head
        while curr:
            copyNode = hashmap[curr]
            copyNode.next = hashmap[curr.next]
            copyNode.random = hashmap[curr.random]
            curr = curr.next

        return hashmap[head]  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that hashmap is used to approach the issue of .random values pointing to nodes further along the LL, and in doing so, allows for quick lookups
- One weak area is that there will have to be two passes of the LL, which can take a while with a large LL, even if simplified, the time complexity is still O(n)