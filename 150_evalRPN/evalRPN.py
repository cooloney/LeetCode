'''
Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def calculate(self, left, op, right):
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return int(float(left) / right)
        else:
            print "Error input op " + op

    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t in "+-*/":
                right = stack.pop()
                left = stack.pop()
                val = self.calculate(left, t, right)
                stack.append(val)
            else:
                stack.append(int(t))
        return stack.pop()

# Test case by myself
s = Solution()
print s.evalRPN(["18", "20", "+"])
print s.evalRPN(["2", "1", "+", "3", "*"])
print s.evalRPN(["4", "13", "5", "/", "+"])
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
