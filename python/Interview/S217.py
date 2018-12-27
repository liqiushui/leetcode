class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = {}
        for e in nums:
            if e in s:
                return True
            else:
                s[e] = e
        return False