class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        if n <= 0 or k <= 0:
            return ret
        self.helper(ret, [], n, k, 1)
        return ret

    def helper(self, result, temp, n, k, pos):
        if len(temp) == k:
            result.append(list(temp))
            return

        for i in range(pos, n + 1):
            temp.append(i)
            self.helper(result, temp, n, k, i + 1)
            temp.pop()


if __name__ == "__main__":
	s = Solution()
	print(s.combine(4, 3))