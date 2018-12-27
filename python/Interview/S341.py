# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIteratorItem(object):
    def __init__(self, arr):
        self.list = arr
        self.cur = 0

    def curObj(self):
        if self.cur < len(self.list):
            e = self.list[self.cur]
            self.cur += 1
            return e
        return None

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = []
        self.nextValue = None
        self.queue.append(NestedIteratorItem(nestedList))
        self.prepare()


    def prepare(self):
        self.nextValue = None
        while self.queue:
            e = self.queue[-1].curObj()
            if not e:
                self.queue.pop()
                continue
            if isinstance(e, list):
                self.queue.append(NestedIteratorItem(e))
            else:
                self.nextValue = e
                return

    def next(self):
        """
        :rtype: int
        """
        e = self.nextValue
        self.prepare()
        print(e)
        return e


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nextValue != None



if __name__ == '__main__':
    print("Hello,World")
    i, v = NestedIterator([[1,1],2,[1,1]]), []
    while i.hasNext():
        e = i.next()
        v.append(e)
    print(v)