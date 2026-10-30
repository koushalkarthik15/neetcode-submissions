class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        def bt(open_,closed_):
            if open_==closed_==n:
                res.append("".join(stack))
                return
            if open_<n:
                stack.append("(")
                bt(open_+1,closed_)
                stack.pop()
            if closed_<open_:
                stack.append(")")
                bt(open_,closed_+1)
                stack.pop()
        bt(0,0)
        return res