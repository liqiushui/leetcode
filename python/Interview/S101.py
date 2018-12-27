# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def cmp(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False
        return node1.val == node2.val

    def isSymmetric2(self, root):
        # 40ms 解法
        def isMirror(left, right):
            if not left and not right:
                return True
            if (not left and right) or (left and not right):
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and \
                   isMirror(left.right, right.left)

        if not root: return True
        return isMirror(root.left, root.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #层序遍历
        l = []
        r = []

        l.append(root)
        r.append(root)

        while len(l) > 0 and len(r) > 0 and self.cmp(l[0], r[0]):
            lt = l.pop(0)
            rt = r.pop(0)

            if lt:
                if lt.left:
                    l.append(lt.left)
                else:
                    l.append(None)

                if lt.right:
                    l.append(lt.right)
                else:
                    l.append(None)

            if rt:
                if rt.right:
                    r.append(rt.right)
                else:
                    r.append(None)

                if rt.left:
                    r.append(rt.left)
                else:
                    r.append(None)

        return not l and not r





if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    s = Solution()
    print(s.isSymmetric(root))