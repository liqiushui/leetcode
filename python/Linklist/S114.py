class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return -1
        slow = head.next
        fast = head.next.next
        while slow and fast and slow != fast:
            print("slow %s fast %s" % (slow.val, fast.val))
            slow = slow.next
            fast = fast.next.next if fast.next else None
        print("slow %s fast %s" % (slow.val, fast.val))
        step = 0
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
            step += 1
        return step


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    s = Solution()
    print(s.detectCycle(head))
