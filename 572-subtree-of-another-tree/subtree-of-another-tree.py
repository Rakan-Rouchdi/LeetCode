# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def sameTree(root, subRoot):
            if not root and not subRoot: # check if the nodes are empty
                return True
            if not root or not subRoot or root.val != subRoot.val: # check if one is empty and the other isnt or the nodes are not equal
                return False
            return (sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)) # recursively check until all nodes are empty (because we processed the whole tree)
        
        if not subRoot: # if subroot is empty (empty tree) return true
            return True
        if not root: # if subroot is not empty but root is empty return false
            return False
        if sameTree(root, subRoot): # both are not empty but check if they are the same tree
            return True
        # if not the same node then check the respective childs of that node and see if they are the same value
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        # Think of sameTree as “Do the trees match starting here?” and isSubtree as “Can I find a match starting anywhere in this tree?”