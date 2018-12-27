class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s.rstrip())-1
        p = l
        while p >= 0:
            if s[p] == ' ':
                break
            p -= 1
        return l - p


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("a "))