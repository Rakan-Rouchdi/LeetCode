# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q: # if both nodes are null then they match (empty trees)
            return True
        if not p or not q or p.val != q.val: # if one node is missing then theres a mismatch
        # or if their values are not equal than there's a mismatch
            return False

        # this means their values match and so now we check their children
        # we first check the left subtree then the right
        # if they are the same both should return true
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        