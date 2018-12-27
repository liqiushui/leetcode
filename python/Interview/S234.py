# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None








class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = self.length(head)
        mid = self.nextNode(head, length / 2 - 1)
        if mid and length >= 2:
            temp = mid.next
            if length %2 == 0:
                mid.next = None
            else:
                mid.next = ListNode(temp.val)
            temp = self.reverseList(temp)
            return self.compare(temp, head)
        return length <= 1

    def length(self, head):
        l = 0
        while head:
            head = head.next
            l += 1
        return l


    def nextNode(self, head, length = 1):
        length = int(length)
        while head and length > 0:
            head = head.next
            length -= 1
        return head


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

    def dump(self, head):
        while head:
            print(str(head.val) + " ", end="")
            head = head.next
        print()

    def compare(self, head1, head2):
        while head1 and head2 and head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        return head1 == None and head2 == None




if __name__ == '__main__':
    s = Solution()
    head = s.makeLinklist([1,2,1])
    print(s.isPalindrome(head))
