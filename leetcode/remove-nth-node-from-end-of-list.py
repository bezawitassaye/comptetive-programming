# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        dummy=ListNode()
        dummy.next=head
        head=dummy
        self.slow=head
        self.fast=head
        while count<n :
            self.fast=self.fast.next
            count+=1

        while self.fast.next:
            self.slow=self.slow.next
            self.fast=self.fast.next

        self.slow.next=self.slow.next.next


        return dummy.next


        


