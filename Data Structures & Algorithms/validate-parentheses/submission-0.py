class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else :
                if len(stack) == 0:
                    return False
                cur_ele = stack.pop()
                if ch == ')' and cur_ele != '(':
                    return False
                elif ch == '}' and cur_ele != '{':
                    return False
                elif ch == ']' and cur_ele != '[':
                    return False

        return len(stack) == 0
