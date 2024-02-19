class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        chec=set()
        for i in range(len(nums)):
            if i not in chec:
                cy=set()
                while True:
                    if i in cy:
                        return True
                    chec.add(i)
                    cy.add(i)      
                    prev,i = i,(i+nums[i])%len(nums)
                    
                    if prev == i :
                        break
                    if nums[prev]>0 != nums[i]<0:
                        break

        return False