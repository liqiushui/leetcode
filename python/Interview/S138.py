# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        def copyNext(head, cache):
            if not head:
                return None
            if head in cache:
                return cache[head]
            next = RandomListNode(head.label)
            cache[head] = next
            next.next = copyNext(head.next, cache)
            next.random = copyNext(head.random, cache)
            return next
        return copyNext(head, {})