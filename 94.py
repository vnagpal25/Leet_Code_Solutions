from typing_extensions import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Iterative Solution
    """
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        stack = [] # represents the call stack
        while curr or stack:
            # keep searching left subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # now have reached a leaf in the left subtree
            # pop the node append to the list
            curr = stack.pop()
            res.append(curr.val)

            # now we need to explore the right subtree in the next iteration
            curr = curr.right
        return res

    """
    Recursive Solution
    """
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     to_ret = []
    #     def inorder(root):
    #         if not root:
    #             return
    #         inorder(root.left)
    #         to_ret.append(root.val)
    #         inorder(root.right)
    #     inorder(root)
    #     return to_ret