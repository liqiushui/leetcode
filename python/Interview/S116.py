# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        def linkRight(left, right):
            if not left:
                return
            left.next = right
            if left.left:
                linkRight(left.left, left.right)
            if left.right:
                if right:
                    linkRight(left.right, right.left)
                else:
                    linkRight(left.right, None)

        linkRight(root, None)
