"""
ListNode class for node organization
"""
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
"""
Doubly LinkedList Class
"""
# class MyLinkedList:

#     def __init__(self):
#         self.head = ListNode(-1)

#     def get(self, index_: int) -> int:
#         curr = self.head
#         index = -1
#         while curr:
#             if index + 1 == index_ and curr.next:
#                 return curr.next.val
#             index += 1
#             curr = curr.next
#         return -1

#     def addAtHead(self, val: int) -> None:
#         self.head.next = ListNode(val, self.head.next, self.head)


#     def addAtTail(self, val: int) -> None:
#         curr = self.head
    
#         while curr.next:
#             curr = curr.next
        
#         curr.next = ListNode(val, None, curr)


#     def addAtIndex(self, index_: int, val: int) -> None:
#         curr = self.head
#         index = -1
#         while curr:
#             if index + 1 == index_:
#                 curr.next = ListNode(val, curr.next, curr)
#                 if curr.next.next:
#                     curr.next.next.prev = curr
#                 return

#             curr = curr.next
#             index += 1
        


#     def deleteAtIndex(self, index_: int) -> None:
#         curr = self.head
#         index = -1
#         while curr:
#             if index + 1 == index_:
#                 if curr.next and curr.next.next:
#                     curr.next = curr.next.next
#                     curr.next.prev = curr
#                 else:
#                     curr.next = None
       
#                 return

#             curr = curr.next
#             index += 1

""" 
Singly LinkedList Class
"""
# class MyLinkedList:

#     def __init__(self):
#         self.head = None

#     def get(self, index_: int) -> int:
#         if self.head is not None:
#             node = self.head # head
#             index = 0
#             while node:
#                 if index == index_:
#                     return node.val
#                 node = node.next
#                 index += 1
#         return -1

#     def addAtHead(self, val: int) -> None:
#         self.head = ListNode(val, self.head)

#     def addAtTail(self, val: int) -> None:
#         if self.head is None:
#             self.head = ListNode(val, None)
#         else:
#             node = self.head
#             while node.next:
#                 node = node.next
#             node.next = ListNode(val, None)

#     def addAtIndex(self, index_: int, val: int) -> None:
        
#         if self.head is None and index_ == 0:
#             self.head = ListNode(val, None)
#         else:
#             index = 0

#             if index == index_:
#                 newNode = ListNode(val, self.head)
#                 self.head = newNode
#                 return

#             node = self.head
#             while node:
#                 if index + 1 == index_:
#                     newNode = ListNode(val, node.next)
#                     node.next = newNode
#                     return
                
#                 node = node.next
#                 index += 1


#     def deleteAtIndex(self, index_: int) -> None:
#         if self.head is None:
#             return
#         index = 0

#         if index == index_:
#             self.head = self.head.next
#             return

#         node = self.head
#         while node:
#             if index + 1 == index_ and node.next:
#                 # node to delete isthe next node
#                 # either it has an element following it, or not
                    
#                 node.next = node.next.next
                
                
#                 return
#             node = node.next
#             index += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)