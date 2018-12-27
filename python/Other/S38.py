class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = self.countSay("1")
        while n > 1:
            x = self.countSay(x)
            n -= 1

        return x


    def countSay(self, n):
        rst = ""
        i = 0
        while i < len(n):
            j = i + 1
            while j < len(n) and n[j] == n[i]:
                j += 1
            rst += (str((j - i)) + str(n[i]))
            i = j
        return rst



if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(4))
