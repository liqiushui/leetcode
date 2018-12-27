class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        order = 0
        for c in s:
            if c in map:
                map[c] = (map[c][0] + 1, map[c][1], c)
            else:
                map[c] = (1, order, c)
            order = order + 1

        max_order = len(s)*2 + 1
        for x in map:
            v = map[x]
            if v[0] == 1:
                max_order = min(max_order, v[1])
        return max_order if max_order < len(s) else -1




if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar("loveleetcode"))