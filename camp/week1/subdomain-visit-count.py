from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_dict = {}
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            subdomains = domain.split(".")
            
            curr_subdomain = ""
            for i in range(len(subdomains) - 1, -1, -1):
                if curr_subdomain == "":
                    curr_subdomain = subdomains[i]
                else:
                    curr_subdomain = subdomains[i] + "." + curr_subdomain
                
                if curr_subdomain in count_dict:
                    count_dict[curr_subdomain] += int(count)
                else:
                    count_dict[curr_subdomain] = int(count)
        
        result = []
        for subdomain, count in count_dict.items():
            result.append(str(count) + " " + subdomain)
        
        return result