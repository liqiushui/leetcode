# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def middleTree(nums, start, end):
            if start > end:
                return None
            mid = int(start + (end - start)/2)
            node = TreeNode(nums[mid])
            node.left = middleTree(nums, start, mid-1)
            node.right = middleTree(nums, mid + 1, end)
            return node

        return middleTree(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    root = Solution().sortedArrayToBST([-10,-3,0,5,9])
    print(root)