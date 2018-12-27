class Solution:
    def isHappy(self, n):
        def happySum(n):
            sum = 0
            while n:
                sum += int(n%10)**2
                n = int(n/10)
            return sum
        self.s = {}
        while n != 1:
            print(n)
            n = happySum(n)
            if n in self.s:
                break
            else:
                self.s[n] = True

        return n == 1


if __name__ == '__main__':
    print(Solution().isHappy(2))