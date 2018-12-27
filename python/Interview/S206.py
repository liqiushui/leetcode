# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head = self.reverseNode(None, head)
        return head

    def reverseNode(self, pre, cur):
        next = None if not cur else cur.next
        if cur:
            cur.next = pre
            return self.reverseNode(cur, next)
        else:
            return pre


if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    head = Solution().reverseList(head)

    print(head)
