class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode(None)
        p = head
        while 1:
            if l1 == l2 == None:
                return head.next
            if l1 == None or (l2 != None and l2.val <= l1.val):
                p.next = ListNode(l2.val)
                p = p.next
                l2 = l2.next
                continue
            if l2 == None or (l1 != None and l1.val <= l2.val):
                p.next = ListNode(l1.val)
                p = p.next
                l1 = l1.next
                continue
# conditions. focus on their order
