# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tmp = head.next
        self.swapLinklist(None, head, head.next)
        return tmp

    def swapLinklist(self, lastTail, first, second):
        if first and second:
            if lastTail:
                lastTail.next = second
            first.next = second.next
            second.next = first
            return self.swapLinklist(first, first.next, None if not first.next else first.next.next)