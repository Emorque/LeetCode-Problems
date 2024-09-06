class ListNode: 
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
        node.prev = tailPrev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)