# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def isSymmetric(self, root):
        def compareSides(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 and root2 and (root1.val == root2.val):
                return compareSides(root1.left, root2.right) and compareSides(root1.right, root2.left)
            else:
                return False

        return compareSides(root.left, root.right)







