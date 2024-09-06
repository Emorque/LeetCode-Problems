1. Share questions you would ask to help understand the question:
- Does the value in following puts always increase by 1?
- Will the keys be unique values?

2. List out 2-3 types of problems that we might consider and our belief of match: Likely, Neutral, Unlikely
- LL (Likely)
- Hashmap (Likely)

3. Write out in plain English what you want to do: 
- I think breaking down this problem will make it easier to understand. 
- First, the init wants to create a cache with a certain capacity. Since, the get and put must be in O(1) complexity, this capacity should be kept as an int that is decremented until it will reach 0. 
- For the get, the value of the key is returned if it exists. Because of the wording, this immediately makes me think of a hashmap, which the key will be the key and the value will be the value
- For put, it gets a bit tricky
  - First, the value of the key must be updated if it exists
  - Second, if the number of keys is greater than capacity, then remove the LRU. 
    - Now, the LRU key needs to be tracked at all times. A key gets "more recently used" if it is used in get or put
    - Thinking about other data structures, stacks, arrays, they require O(n) to first find the key, and then would have to be shifted in at at least O(n) to change a key's position in the used queue
      - A queue is on the right step, but a LL might be better, since if its Doubly linked, I can used a prev and next pointer to easily shift orders. 
- It comes down to creating a DLL class, that has a head and a tail, with the head as the LRU side, and the Tail as the MRU side, with next and prev pointers allowing for easy order changes

4. Translate each sub-problem into pseudocode:
- class ListNode (self, val, key):
  - self.val = val
  - self.key = key
  - self.next = None
  - self.prev = None

- def __init__(self, capacity: int):
  - self.capacity = capacity 
  - self.head, self.tail = ListNode(0), ListNode(0)
  - self.head.next = self.tail 
  - self.tail.prev = self.head
  - self.cache = {}

- def get(self, key: int) -> int:
  - if key not in hashmap:
    - return -1
  - currNode = hashmap[key]
  - prev = currNode.prev 
  - next = currNode.next
  - prev.next = next
  - next.prev = prev

  - tailPrev = self.tail.prev
  - tailPrev.next = currNode
  - currNode.next = tail
  - tail.prev = currNode
  - currNode.prev = tailPrev

  - return currNode.val

- def put(self, key: int, value: int) -> None:
  - if key in cache:
    - remove key from LL
  - self.cache[key] = ListNode(value)
  - add key to LL

  - self.capacity -= 1
  - if self.capacity <= -1
    - delNode = head.next
    - newNext = delNode.next
    - head.next = newNext
    - newNext.prev = head
    - del cache[delNode.key]

5. Translate the pseudocode into Python and share your final answer:
  <!-- class ListNode: 
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

  class LRUCache:
      def __init__(self, capacity: int):
          self.cache = {}
          self.capacity = capacity
          self.head, self.tail = ListNode(0,0), ListNode(0,0)
          self.head.next = self.tail
          self.tail.prev = self.head

      def get(self, key: int) -> int:
          if key not in self.cache:
              return -1
          currNode = self.cache[key]

          self.removeNode(currNode)
          self.addNode(currNode)

          return currNode.val

      def put(self, key: int, value: int) -> None:
          if key in self.cache:
              self.removeNode(self.cache[key])
          self.cache[key] = ListNode(key, value)
          self.addNode(self.cache[key])

          if len(self.cache) > self.capacity:
              delNode = self.head.next
              newNext = delNode.next
              self.head.next = newNext
              newNext.prev = self.head 

              del self.cache[delNode.key]

      def removeNode(self, node: ListNode):
          prevNode = node.prev
          nextNode = node.next

          prevNode.next = nextNode
          nextNode.prev = prevNode

      def addNode(self, node: ListNode): 
          tailPrev = self.tail.prev
          tailPrev.next = node
          node.next = self.tail
          self.tail.prev = node
          node.prev = tailPrev  -->

6. Share at least one strong/weak area of your algorithm or future potential work:
- One strong area is that thanks to hashmap lookups and the constant number of LL node shifts for get and put, the functions get and put are in O(1)
- One weak area is that it can get hard to follow. I had to make two helper functions addNode and removeNode, after making similar node shifts in both get and put. This also makes it a bit harder to follow. 