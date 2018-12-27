class Solution15:
    def __init__(self):
        self.result = []

    def threeSum(self, nums, target=0):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cp = sorted(list(nums))
        i = 0
        while i < len(cp) - 2:
            if i > 0 and cp[i] == cp[i-1]:
                i += 1
                continue
            temp = []
            self.twoSum(cp[i+1:], temp, target-cp[i])
            for e in temp:
                e.append(cp[i])
            self.result = self.result + temp
            i += 1
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


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        cp = sorted(nums)
        print(cp)
        i = 0
        while i < len(cp):
            if i > 0 and cp[i] == cp[i-1]:
                i += 1
                continue
            s3 = Solution15()
            for x in s3.threeSum(cp[i+1:], target - cp[i]):
                tmp = ([cp[i]] + x)
                ret.append(tmp)
                print(cp[i])
                print(cp[i+1:])
                print(tmp)
                print()
            i += 1
            print(ret)


if __name__ == '__main__':
    s = Solution()
    s.fourSum([1,0,-1,0,-2,2], 0)