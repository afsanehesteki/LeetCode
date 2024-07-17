#21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://www.youtube.com/watch?v=XIdigk956u0&ab_channel=NeetCode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        list3= ListNode()
        cur3= list3

        while cur1 and cur2: 
            if cur1.val <=cur2.val:
                cur3.next = cur1
                cur1 = cur1.next
            else:
                cur3.next = cur2
                cur2 = cur2.next
            
            cur3 = cur3.next

        if cur1: 
            cur3.next = cur1
        elif cur2:
            cur3.next = cur2

        return list3.next
        
