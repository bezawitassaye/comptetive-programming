class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros=0
        ones=0
        zer=[]
        one=[]
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros+=1
                zer.append(zeros)
            else:
                zer.append(zeros)
        zer.insert(0,0)        
        nums=nums[::-1]
        for j in range(len(nums)):
            if nums[j] ==1:
                ones+=1
                one.append(ones)
            else:
                one.append(ones)
        one.reverse()
        one.append(0)
        for k in range(len(one)):
            temp=one[k]
            one[k] = temp + zer[k]
        maxx=max(one)
        final=[l for l in range(len(one)) if one[l] == maxx]
        return final   

                            