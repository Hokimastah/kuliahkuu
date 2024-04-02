class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        y = [char for char in s]
        stack = []
        hasil = []
        for i,x in enumerate(y):
            if not stack : stack.append(x)
            elif x == "(":
                stack.append(x)
            elif x == ")":
                if len(stack) == 1:
                    stack.pop()
                elif stack.count('(') == stack.count(')')+1:
                    stack.pop(0)
                    for k in stack:
                        hasil.append(k)
                    stack = []
                else:
                    stack.append(x)

        output = "".join(hasil)
        return output