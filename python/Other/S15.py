class Solution:


    def __init__(self):
        self.result = []

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cp = sorted(list(nums))
        print(cp)
        i = 0
        while i < len(cp) - 2:
            if i > 0 and cp[i] == cp[i-1]:
                i += 1
                continue
            temp = []
            self.twoSum(cp[i+1:], temp, -cp[i])
            for e in temp:
                e.append(cp[i])
                print(cp[i])
                print(e)
                print()
            self.result = self.result + temp
            i += 1
        print(self.result)
        return self.result


    def twoSum(self, nums, result, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                result.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1






if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
