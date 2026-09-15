class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialize and populate the stack with integers. when we find an operator, compute and append the result to the stack.
        stack = []

        for ch in tokens:
            if ch in "+-*/":
                r = stack.pop()
                l = stack.pop()

                if ch == "+":
                    stack.append(l + r)
                elif ch == "-":
                    stack.append(l - r)
                elif ch == "/":
                    stack.append(int(float(l / r)))
                else:
                    stack.append(l * r)
            else:
                stack.append(int(ch))
        
        return stack.pop()
