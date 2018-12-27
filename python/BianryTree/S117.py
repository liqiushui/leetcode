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
        head = TreeLinkNode(-1)
        pre = head

        while root:
            if root.left:
                pre.next = root.left
                pre = pre.next

            if root.right:
                pre.next = root.right
                pre = pre.next

            root = root.next

            if not root:
                pre = head
                root = head.next
                head.next = None
