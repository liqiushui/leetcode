class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        last = None

        while i < len(nums) and j < len(nums):
            if last != nums[j]:
                nums[i] = nums[j]
                last = nums[i]
                i += 1
            j += 1
        return i


if __name__ == '__main__':
    s = Solution()
    x = [1,1,2]
    print(s.removeDuplicates(x))
    print(x)



