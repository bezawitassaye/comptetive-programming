class Node:
    def __init__(self, value,next,prev):
        self.value = value
        self.next = next
        self.prev=prev

class MyCircularQueue:
   
    def __init__(self, k: int):
        self.left=Node(0,None,None)
        self.right=Node(0,None,self.left)
        self.left.next=self.right
        self.k=k

    def enQueue(self, value: int) -> bool:
        if self.isFull():return False

        current=Node(value,self.right,self.right.prev)
        self.right.prev.next=current
        self.right.prev=current
        self.k-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next=self.left.next.next
        self.left.next.prev=self.left
        self.k+=1
        return True

          


    def Front(self) -> int:
        if self.isEmpty(): return -1 
        return self.left.next.value
    
    def Rear(self) -> int:
        if self.isEmpty(): return -1  
        return self.right.prev.value  

        

    def isEmpty(self) -> bool:
        return self.left.next == self.right
        

    def isFull(self) -> bool:
        return self.k ==0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()