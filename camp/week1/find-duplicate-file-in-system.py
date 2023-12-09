from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_map = {}  # hashmap to store file content and paths
        
        for path in paths:
            directory, *files = path.split(' ')
            
            for file in files:
                file_name, content = file.split('(')
                content = content[:-1]  # remove closing parenthesis
                
                file_path = directory + '/' + file_name
                if content in file_map:
                    file_map[content].append(file_path)
                else:
                    file_map[content] = [file_path]
        
        result = []
        for content, paths in file_map.items():
            if len(paths) > 1:
                result.append(paths)
        
        return result