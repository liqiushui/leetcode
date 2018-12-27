class Solution:


    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        r = [str(i+1) for i in range(n)]
        print(r)
        factorial = [1] * (n + 1)
        for i in range(1, n+1):
            factorial[i] = factorial[i-1]*i
        print(factorial)

        ret = ""
        k -= 1
        for i in range(1, n+1):
            index = int(k/factorial[n-i])
            num = r[index]
            ret += num
            r.remove(num)
            k -= index*factorial[n-i]
        return ret

    def ermutation(self, nums, index):
        if index < len(nums):
            for i in range(index, len(nums)):
                nums[index],nums[i] = nums[i],nums[index]
                self.ermutation(nums, index+1)
                nums[index], nums[i] = nums[i], nums[index]

        else:
            print(nums)




if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(4,9))