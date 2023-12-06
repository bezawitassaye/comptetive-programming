class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        hashset={}
        for i in list1:
            if i in list2:
                hashset[i]=list1.index(i)+list2.index(i)
            else:
                continue
        min_value=min(hashset.values())

        min_key=[key for key,value in hashset.items() if value==min_value]
        return min_key               