import math

class Solution:
    def __init__(self):
        pass

    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        return 0

    def applyOperation(self, b, a, op):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a // b

    def calculate(self, s: str) -> int:
        values = []
        operators = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            elif s[i] == '(':
                operators.append(s[i])
            elif s[i].isdigit():
                value = 0
                while i < len(s) and s[i].isdigit():
                    value = (value * 10) + int(s[i])
                    i += 1
                values.append(value)
                i = i - 1
            elif s[i] == ')':
                while len(operators) != 0 and operators[-1] != '(':
                    values.append(self.applyOperation(values.pop(), values.pop(), operators.pop()))
                operators.pop()
            else:
                while len(operators) != 0 and self.precedence(operators[-1]) >= self.precedence(s[i]):
                    values.append(self.applyOperation(values.pop(), values.pop(), operators.pop()))
                operators.append(s[i])
            i += 1

        while len(operators) != 0:
            values.append(self.applyOperation(values.pop(), values.pop(), operators.pop()))

        return values[-1]


sol = Solution()
print(sol.calculate(" 3/2 "))
