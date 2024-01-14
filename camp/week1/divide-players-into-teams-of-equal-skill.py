class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
    
        skill.sort()
        l=0
        check=0
        r=len(skill)-1
        hashset={}
        hashset2={}
        count=0
        if len(skill) == 2:
            return skill[0]*skill[1]
        else:
            while l < r:
                hashset[count]=skill[l]*skill[r]
                hashset2[count]=skill[l]+skill[r]
                count+=1
                l+=1
                r-=1
        if len(set(hashset2.values())) == 1:
            for value in hashset.values():
                check+=value
            
            return check   
        else:
            return -1    



     

            
        