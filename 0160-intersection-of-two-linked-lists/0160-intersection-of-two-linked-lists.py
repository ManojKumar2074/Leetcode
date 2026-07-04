# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        tempA = headA
        tempB = headB
        
        while tempA != tempB:
            if tempA:
                tempA = tempA.next
            else:
                tempA = headB  # Reset to the head of the opposite list
                
            if tempB:
                tempB = tempB.next
            else:
                tempB = headA  # Reset to the head of the opposite list
                
        return tempA