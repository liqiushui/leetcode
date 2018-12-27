class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return path
        s = path.split("/")
        r = []
        for i in range(0, len(s)):
            if s[i] == '' or s[i] == '.':
                continue
            elif s[i] == '..':
                if r:
                    r.pop()
            else:
                r.append(s[i])
        print(r)
        return "/"+"/".join(r)


if __name__ == '__main__':
    s = Solution()
    # print(s.simplifyPath("/home/"))
    print(s.simplifyPath("/a//b////c/d//././/.."))
