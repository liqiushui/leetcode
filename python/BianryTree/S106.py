# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(inorder, postorder):
            if not inorder:
                return None

            # pick up the first element as a root
            root_val = postorder.pop()
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = inorder.index(root_val)

            # recursion
            root.right = helper(inorder[index + 1:], postorder)
            root.left = helper(inorder[:index], postorder)

            return root

        return helper(inorder, postorder)



if __name__ == '__main__':
    s = Solution()
    r = s.buildTree([9,3,15,20,7], [9,15,7,20,3])
    print(r)
