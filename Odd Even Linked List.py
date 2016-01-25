class Solution(object):
    def oddEvenList(self, head):
        if head == None:
            return None
        p = head
        n = 0
        while p != None:
            p = p.next
            n += 1
        if n == 1:
            return head

        oddhead = head
        evenhead = head.next
        oddp = oddhead
        evenp = evenhead

        for i in range(int(n/2) - 1):
            oddp.next = evenp.next
            oddp = oddp.next
            evenp.next = oddp.next
            evenp = evenp.next
        if n % 2 == 1:
            oddp.next = evenp.next
            oddp = oddp.next

        oddp.next = evenhead
        evenp.next = None

        return oddhead
