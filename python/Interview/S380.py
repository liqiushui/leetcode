import random

class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.content = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        print("insert " + str(val))
        if not val in self.map:
            self.content.append(val)
            self.map[val] = len(self.content) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        print(val)
        if val in self.map:
            delTarPos = self.map[val]
            lastPos = len(self.content) - 1
            lastVal = self.content[-1]
            self.content[lastPos], self.content[delTarPos] = self.content[delTarPos], self.content[lastPos]
            self.map[val] = lastVal
            self.map[lastVal] = delTarPos
            self.content.pop()
            self.map.pop(val, None)
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.content) > 0:
            return self.content[random.randint(0, len(self.content) - 1)]
        return 0


if __name__ == '__main__':
    s = RandomizedSet()
    op = ["RandomizedSet","insert","insert","remove","insert","insert","insert","remove","remove","insert","remove","insert","insert","insert","insert","insert","getRandom","insert","remove","insert","insert"]
    value = [[],[3],[-2],[2],[1],[-3],[-2],[-2],[3],[-1],[-3],[1],[-2],[-2],[-2],[1],[],[-2],[0],[-3],[1]]
    print(len(op))
    print(len(value))
    for i in range(0, len(op)):
        if op[i] == "insert":
            s.insert(value[i][0] if len(value[i]) > 0 else 0)
        if op[i] == "remove":
            s.remove(value[i][0] if len(value[i]) > 0 else 0)
        if op[i] == "getRandom":
            print(s.getRandom())
