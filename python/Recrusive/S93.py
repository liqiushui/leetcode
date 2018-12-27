class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []
        ret = []
        self.helper(s, 0, [], ret)
        return ret

    def helper(self, s, pos, temp, result):
        limit = 4
        if len(temp) == limit and pos == len(s):
            result.append(".".join(list(temp)))
            return
        if len(temp) >= limit:
            return
        i = pos
        x = 0
        while i + x < (len(s) + 1) and x <= 3:
            t = s[i:i + x]
            if self.isValid(t) and len(temp) < 4:
                temp.append(t)
                self.helper(s, pos + x, temp, result)
                temp.pop()
            x += 1

    def isValid(self, s):
        if len(s) >= 1 and len(s) <= 3:
            if len(s) > 1 and s[0] == '0':
                return False
            n = int(s)
            return n >= 0 and n <= 255
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses("010010"))