class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        ss=[]

        for i in range(1,len(salary)-1):
            ss.append(salary[i])
        return sum(ss)/len(ss)    
        