# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        current = head
        is_sorted = False

        while not is_sorted:
            is_sorted = True
            current = head

            while current.next:
                if current.val > current.next.val:
                    temp = current.val
                    current.val = current.next.val
                    current.next.val = temp
                    is_sorted = False
                current = current.next

        return head  



        