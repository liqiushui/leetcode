class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        nums = list(map(lambda x: str(x), list(range(1, n + 1))))
        for i in range (3, n + 1, 3):
            nums[i-1] = "Fizz"
        for i in range (5, n + 1, 5):
            if i % 3 == 0:
                nums[i-1] = "FizzBuzz"
            else:
                nums[i-1] = "Buzz"


        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))
