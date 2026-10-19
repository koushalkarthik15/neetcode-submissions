class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operator={
            "+":lambda b,a:b+a,
            "-":lambda b,a:b-a,
            "*":lambda b,a:b*a,
            "/":lambda b,a:int(b/a)
        }
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else:
                a=int(stack.pop())
                b=int(stack.pop())
                ans=operator[token](b,a)
                stack.append(ans)
        return stack[-1]
