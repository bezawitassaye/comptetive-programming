class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        r=len(letters)-1
        m=0
        while l<=r:
            m=(l+r)//2
            
            if letters[m] <= target:
                l=m+1    
            else:
                r=m-1
        if l < len(letters):
            return  letters[l]
        return letters[0]               
