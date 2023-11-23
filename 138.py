"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # maps og nodes to new nodes
        # mapping null to null to avoid key errors for curr.next and curr.random
        nodes_map = {None : None} 


        # first pass through the list
        # maps old nodes to new nodes
        curr = head
        while curr:
            deep_copy = Node(curr.val)
            nodes_map[curr] = deep_copy
            curr = curr.next

        # second pass through the list connects new node's pointers (next and random)
        curr = head
        while curr:
            deep_copy = nodes_map[curr]
            deep_copy.next = nodes_map[curr.next]
            deep_copy.random = nodes_map[curr.random]
            curr = curr.next
        
        # return 
        return nodes_map[head]
