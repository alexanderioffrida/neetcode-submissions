class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return False

        stack = []

        close_open = { ")" : "(", "]" : "[", "}" : "{",}

        for ch in s:
            if ch in close_open:
                if stack and stack[-1] == close_open[ch]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(ch)
        
        return True if not stack else False
