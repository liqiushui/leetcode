class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        print(str(x))
        print(str(x)[::-1])
        return str(x) == str(x)[::-1]



if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))