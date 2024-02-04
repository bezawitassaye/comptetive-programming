class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        elem=0
        l=0
        r=len(people)-1
        people.sort()
        while l < r:
            if people[l] + people[r] <= limit:
                l+=1
                r-=1
                elem+=2
                count+=1
            else:
                r-=1
                count+=1
                elem+=1
        print(len(people),elem)        
        if count>0:
            return count+(len(people)-elem)
        else:
            return -1                
        