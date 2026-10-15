class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = {
            "+": lambda x, y: y + x,
            "-": lambda x, y: y - x,
            "*": lambda x, y: y * x,
            "/": lambda x, y: int(y / x) 
        }
        for token in tokens:
            if token not in operation:
                stack.append(int(token))
            else:
                stack.append(operation[token](stack.pop(), stack.pop())) 
        return stack[0]