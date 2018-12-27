class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        num = 0
        length = len(s)
        i = 0
        while i < length:
            print(s[i])
            if s[i] == 'I':
                if i+1 < length and s[i+1] == 'V':
                    num += 4
                    i += 2
                    continue
                elif i+1 < length and s[i+1] == 'X':
                    num += 9
                    i += 2
                    continue
                else:
                    num += 1
            elif s[i] == 'V':
                num += 5
            elif s[i] == 'X':
                if i+1 < length and s[i+1] == 'L':
                    num += 40
                    i += 2
                    continue
                elif i+1 < length and s[i+1] == 'C':
                    num += 90
                    i += 2
                    continue
                else:
                    num += 10
            elif s[i] == 'L':
                num += 50
            elif s[i] == 'C':
                if i+1 < length and s[i+1] == 'D':
                    num += 400
                    i += 2
                    continue
                elif i+1 < length and s[i+1] == 'M':
                    num += 900
                    i += 2
                    continue
                else:
                    num += 100
            elif s[i] == 'D':
                num += 500
            elif s[i] == 'M':
                num += 1000
            else:
                pass
            i += 1

        return num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt("MCMXCIV"))