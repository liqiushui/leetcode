# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        lenA = self.getLinklistLen(headA)
        lenB = self.getLinklistLen(headB)
        if not lenA or not lenB:
            return None
        diff = 0
        if lenA >= lenB:
            diff = lenA - lenB
            while diff > 0:
                headA = headA.next
        else:
            diff = lenB - lenA
            while diff > 0:
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getLinklistLen(self, head):

        len = 0
        while head:
            len = len + 1
            head = head.next
        return len


    def makeLinklist(self, nums):
        head = None
        last = head
        for num in nums:
            if not head:
                head = ListNode(num)
                last = head
            else:
                last.next = ListNode(num)
                last = last.next
        return head


    def getLinklistTail(self, head):
        while head and head.next:
            head = head.next
        return head

if __name__ == '__main__':
    s = Solution()

    head1 = s.makeLinklist([1,2,3,4,5,6])
    head2 = s.makeLinklist([7,8,9])
    s.getLinklistTail(head2).next = head1.next

    print(s.getLinklistLen(head1))
    print(s.getLinklistLen(head2))