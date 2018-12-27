class Solution(object):

    def __init__(self):
        self.mark = set()

    def wordBreak(self, s, wordDict):

        if not self.mark:
            for x in wordDict:
                self.mark.add(x)

        result = False
        for i in range(1,len(s)+1):
            left = s[:i]
            right = s[i:]
            # print("left = %s, right = %s" % (left, right))

            if not left or left in self.mark:
                result = result or (not right or self.wordBreak(right, wordDict))

            if result:
                break

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak("aaaaaaa", ["aaaa","aaa"]))