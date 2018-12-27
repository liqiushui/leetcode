class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return b if b else a
        ca = a[::-1]
        cb = b[::-1]
        ret = ""
        ia = 0
        ib = 0
        last = 0
        lenca = len(ca)
        lencb = len(cb)
        while ia < lenca or ib < lencb:

            ea = int(ca[ia]) if ia < lenca else 0
            eb = int(cb[ib]) if ib < lencb else 0
            sum = last + ea + eb
            ret += str(sum%2)
            last = int(sum/2)

            ia += 1
            ib += 1
        if last > 0:
            ret += str(last)
        return ret[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))