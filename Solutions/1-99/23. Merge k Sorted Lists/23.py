# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode: 
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for node in lists:
            if node:            
                heapq.heappush(minHeap, HeapNode(node))

        res = ListNode()
        curr = res

        while minHeap:
            heapNode = heapq.heappop(minHeap).node
            curr.next = heapNode
            curr = curr.next
            if heapNode.next:
                heapq.heappush(minHeap, HeapNode(heapNode.next))

        return res.next
        