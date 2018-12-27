class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None


        def operate(right, left, oper):
            if oper == "+":
                return int(left + right)
            if oper == "-":
                return int(left - right)
            if oper == "*":
                return int(left * right)
            if oper == "/":
                return int(left / right)


        stack = []
        while tokens:
            token = tokens.pop(0)
            if token in ["+", "-", "*", "/"]:
                stack.append(operate(stack.pop(), stack.pop(), token))
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))