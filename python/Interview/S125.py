import re
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]',"", s)
        copy = s[::-1]
        print(copy)
        print(s)
        return copy == s



if __name__ == '__main__':
    print(Solution().isPalindrome("0P"))