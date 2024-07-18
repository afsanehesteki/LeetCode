# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        myDeque = collections.deque()
        cur = head
        while cur !=None:
            myDeque.append(cur)
            cur = cur.next
        while len(myDeque)>1:
            topRight = myDeque.pop().val
            topLeft = myDeque.popleft().val
            if topRight!=topLeft:
                return False
        
        return True
