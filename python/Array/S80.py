class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 2:
            return length
        nums = sorted(nums)
        print(nums)
        i = 0
        j = 0
        last_num = None
        last_num_count = 0
        while j < length:
            if nums[j] != last_num or (nums[j] == last_num and last_num_count <= 1):
                last_num_count = 1 if nums[j] != last_num else last_num_count + 1
                last_num = nums[j]
                print(nums[j])
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                last_num = nums[j]
                last_num_count += 1
                j += 1
        print(nums)
        return i


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))