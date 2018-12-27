class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        d = {}
        for e in strs:
            index = 0
            for c in e:
                key = c + str(index)
                d[key] = (d[key] + 1) if key in d else 1
                index += 1
        l = len(strs)
        ret = ""
        if strs:
            index = 0
            for x in strs[0]:
                key = str(x) + str(index)
                if d[key] == l:
                    ret += x
                else:
                    break
                index += 1
        return ret



if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["aa","aa"]))