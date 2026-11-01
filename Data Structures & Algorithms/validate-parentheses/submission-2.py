class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        b_map = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in b_map:
                stack.append(b_map[i])
            else:
                if not stack or stack.pop() != i:
                    return False
        return not stack  
