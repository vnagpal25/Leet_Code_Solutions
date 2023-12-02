# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        The idea here is that performing DFS on a binary search tree returns
        the inorder traversal of the tree

        1) So, we have to traverse as far left as possible (this is the smallest value in the tree/subtree). This is the 1st node that we are going to explore.
        2) The second node that we are going is the parent of that node
        3) The third node that we explore is the smallest child in the right child's left subtree. This is a repeat of 1)

        Each time we explore a node(pop it from the stack), we increment our counter by 1
        Once this counter reaches k, we return the node's value.


        """


        n = 0        
        curr = root
        stack = []
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right