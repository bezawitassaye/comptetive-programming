class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        stack=[]
        for i in range(len(path)):
            if path[i] == "..":
                if stack:
                    stack.pop()
            if path[i] not in ("",".",".."):
                stack.append(path[i])
               
        return "/" + "/".join(stack)               


        