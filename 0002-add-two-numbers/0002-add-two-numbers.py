# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == 0  and l2 == 0:
            return 0
        t1 = l1
        t2 = l2
        dummy = ListNode(-1)
        curr = dummy
        carry = 0

        while t1 or t2 or carry:
            summ = carry
            if t1:
                summ = summ + t1.val
                t1 = t1.next
            if t2:
                summ = summ + t2.val
                t2 = t2.next

            curr.next = ListNode(summ % 10)
            carry = summ // 10
            curr = curr.next
        return dummy.next

