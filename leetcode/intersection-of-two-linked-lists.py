# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashset=set()

        curr1 = headA
        curr2 = headB
        
        while curr1:
            hashset.add(curr1)
            curr1=curr1.next
        while curr2:
            if curr2 in hashset:
                return curr2
            curr2=curr2.next        
        return None
            
     