class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # from end to start
        pLast = m + n - 1

        while pLast >= 0 and m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[pLast] = nums1[m-1]
                m = m - 1
            else:
                nums1[pLast] = nums2[n-1]
                n = n - 1
            pLast = pLast - 1

        return nums1


