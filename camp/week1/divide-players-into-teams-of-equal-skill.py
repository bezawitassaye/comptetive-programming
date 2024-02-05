class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        k=sum(skill)*2//len(skill)
        pro=0
        l=0
        r=len(skill)-1
        while l<r:
            if skill[l]+skill[r] ==k:
                count=skill[l]*skill[r]
                pro+=count
            else:
                return -1
            l+=1
            r-=1
        return pro            
    
        
     

            
        