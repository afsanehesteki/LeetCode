# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        cur = head
        while cur:
            if cur.next in s:
                return True
            s.add(cur)
            cur = cur.next
        return False
