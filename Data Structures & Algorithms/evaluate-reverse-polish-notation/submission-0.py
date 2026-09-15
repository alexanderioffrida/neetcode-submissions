class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initialize and populate the stack with integers. when we find an operator, compute and append the result to the stack.
        stack = []

        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "*":
                stack.append(stack.pop() * stack.pop())
            elif ch == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b / a)))
            elif ch == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            else: stack.append(int(ch))
        return stack.pop()
