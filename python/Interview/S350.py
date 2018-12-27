class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = {}
        s2 = {}

        for i in nums1:
            if not i in s1:
                s1[i] = 1
            else:
                s1[i] = s1[i] + 1

        for i in nums2:
            if not i in s2:
                s2[i] = 1
            else:
                s2[i] = s1[i] + 1

        result = []
        for k,v in s1:
            if k in s2:
                result = result + [k] * min(v, s2[k])

        return result