class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        if not A:
            return 0

        hashA = {}
        for a in A:
            for b in B:
                key = (a + b)
                hashA[key] = 1 if not key in hashA else (hashA[key] + 1)
        hashB = {}
        for c in C:
            for d in D:
                key = (c + d)
                hashB[key] = 1 if not key in hashB else (hashB[key] + 1)

        ret = 0
        for i in hashA.keys():
            if -i in hashB:
                ret = ret + hashA[i] * hashB[-i]
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.fourSumCount([-1,-1], [-1,1], [-1,1], [1,-1]))