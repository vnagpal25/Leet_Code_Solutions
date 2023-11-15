# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iterative solution
class Solution:
    def insert_node_iter(self, node, val):
        # edge case handling
        if node is None:
            return TreeNode(val)
        
        curr = node
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    return node
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    return node
                else:
                    curr = curr.right

    # def insert_node_rec(self, node, val):
    #     # base case for empty tree
    #     if node is None:
    #         return TreeNode(val)
        
    #     # we found an empty spot to place our smaller value into the left subtree
    #     elif (node.left is None and val < node.val):
    #         node.left = TreeNode(val)
    #         return node
        
    #     # we found an empty spot to place our smaller value into the right subtree
    #     elif (node.right is None and val > node.val):
    #         node.right = TreeNode(val)
    #         return node

    #     # we need to recursively search right or left subtree and insert the new node
    #     else:
    #         # smaller values go in left subtree
    #         if val < node.val:
    #             node.left = self.insert_node_rec(node.left, val)
    #             return node
    #         # larger values go in right subtree
    #         else:
    #             node.right = self.insert_node_rec(node.right, val)
    #             return node


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # iterative solution
        return self.insert_node_iter(root, val)

        # recursive solution
        # return self.insert_node_rec(root, val)



        
        