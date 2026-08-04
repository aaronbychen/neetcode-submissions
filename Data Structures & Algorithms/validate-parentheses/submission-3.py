class Solution:
    def isValid(self, s: str) -> bool:
        # '(', ')', '{', '}', '[' and ']'
        if s[0] != '(' and s[0] != '{' and s[0] != '[':
            return False
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return False
                if stack.pop() != '(':
                    return False
            elif c == '}':
                if not stack:
                    return False
                if stack.pop() != '{':
                    return False
            elif c == ']':
                if not stack:
                    return False
                if stack.pop() != '[':
                    return False
        return stack == []