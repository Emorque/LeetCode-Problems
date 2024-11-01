class Node:
    def __init__(self, key: int, value: int, next = None, prev = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.nodes = {}        

    def add(self, node):
        mru = self.head.next
        self.head.next = node
        node.next = mru
        
        mru.prev = node
        node.prev = self.head
    
    def remove(self, node):
        p, n = node.prev, node.next
        
        p.next = n
        n.prev = p

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.remove(self.nodes[key])
        self.add(self.nodes[key])

        return self.nodes[key].value

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key not in self.nodes:
            self.nodes[key] = node
            self.capacity -= 1
            self.add(node)
            if self.capacity < 0: 
                del self.nodes[self.tail.prev.key]
                self.remove(self.tail.prev)
        else:
            self.remove(self.nodes[key])
            self.nodes[key] = node
            self.add(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)