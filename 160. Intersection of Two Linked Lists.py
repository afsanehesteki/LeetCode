# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        cur1 = headA
        cur2 = headB
        if not cur1 or not cur2: 
            return None
        while cur1:
            s.add(cur1)
            cur1=cur1.next
        while cur2:
            if cur2 in s:
                return cur2
            cur2 = cur2.next
        return None

        
