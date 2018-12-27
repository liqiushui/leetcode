class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0

        while i < len(nums) and j < len(nums):
            if val != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i