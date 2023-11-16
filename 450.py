class Solution:
    def rearrangeTree(self, node):
        if node.left is None:
            # we have no left child, so we can just 
            # return the right child
            return node.right

        elif node.right is None:
            # we have no right child so we can just
            # return the left child
            return node.left
        
        # we have 2 children, need to handle both of them
        else:
            # find the largest value in the left subtree of the right child of the node to delete
            # and put it in the place of the node to be deleted

            # current node
            succParent = node
            
            # first right child
            succ = node.right
            
            # find largest value in left tree
            while succ.left is not None:
                succParent = succ
                succ = succ.left
            
            
            if succParent != node:
                # remove node that will be used to replace
                succParent.left = succ.right
            else:
                # remove node that will be used to replace
                succParent.right = succ.right

            # replace the node to delete's value with new value
            node.val = succ.val
            del succ
            return node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # nothing to delete
        if root is None:
            return root
        
        # recursively search for the node in the left subtree 
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # recursively search for the node in the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        # we've found the node
        # let's delete it but ensure that we are rearranging it properly
        else:
            root = self.rearrangeTree(root)

        return root
