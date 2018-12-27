class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1

        return haystack.find(needle)


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("aaaaa", "bba"))