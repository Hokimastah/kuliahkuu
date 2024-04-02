class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        x = [char for char in s]
        stack = []
        hasil = []
        for i in x:
            if not stack : stack.append(i)
            elif i == "(":
                stack.append(i)
            elif i == ")":
                if len(stack) == 1:
                    stack.pop()
                else :
                    hasil.append(stack.pop())
                    hasil.append(i)
        
        output = "".join(hasil)
        print(output)