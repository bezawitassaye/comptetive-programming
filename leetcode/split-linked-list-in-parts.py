# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
       length=0
       curr=head
       while curr:
           curr=curr.next
           length+=1
           
       lengtharr=length//k
       mod=length%k
       arr=[]
       curr=head
       for i in range(k):
           arr.append(curr)
           for j in range(lengtharr - 1 +(1 if mod else 0)):
               if not curr:break 
               curr=curr.next
                  
           mod-= (1 if mod else 0)
           if curr:    
               curr.next,curr=None,curr.next
       return arr                   
              



