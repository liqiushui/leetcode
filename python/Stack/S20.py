class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        q = []
        m = {')':"(", ']':"[", '}':"{"}
        for x in s:
            if x in ['(','[','{']:
                q.append(x)
            else:
                if not q or q.pop() != m[x]:
                    return False
        return len(q) == 0



if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))