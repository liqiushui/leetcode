class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        slist = set(wordList)
        if not endWord in slist:
            return 0
        stepMap = {}
        reach = set()
        wait = [beginWord]
        stepMap[beginWord] = 1
        minstep = None
        while wait:
            cur = wait.pop(0)
            reach.add(cur)
            items = self.transform(cur, slist)
            print("%s %s" % (cur, items))
            print(stepMap)
            print()
            for item in items:
                if not item in stepMap:
                    stepMap[item] = stepMap[cur] + 1

                if item == endWord:
                    minstep = min(stepMap[item], minstep) if minstep else stepMap[item]
                else:
                    if not item in reach and not item in wait:
                        wait.append(item)
        return 0 if not minstep else minstep



    def transform(self, beginWord, slist):
        result = []
        for j in range(len(beginWord)):
            for i in range(97, 97+26):
                rc = chr(i)
                if rc != beginWord[j]:
                    temp = beginWord[:j] + str(rc) + beginWord[j+1:]
                    if temp in slist:
                        result.append(temp)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("qa","sq",["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))

