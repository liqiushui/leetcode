class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._content = []
        self._mininum = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._content.append(x)
        self._mininum.append(x if not self._mininum else min(self._mininum[-1], x))

    def pop(self):
        """
        :rtype: void
        """
        if self._content:
            self._content.pop()
            self._mininum.pop()

    def top(self):
        """
        :rtype: int
        """
        if self._content:
            return self._content[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self._mininum:
            return self._mininum[-1]


if __name__ == '__main__':

    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.pop()

    print(s.getMin())