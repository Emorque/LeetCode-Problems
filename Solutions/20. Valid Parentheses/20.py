class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif len(stack) == 0 and (char == ")" or char == "}" or char == "]"):
                return False
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False
        return len(stack) == 0             