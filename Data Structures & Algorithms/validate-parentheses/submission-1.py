class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapp={']':'[',')':'(','}':'{'}
        for char in s:
            if char in mapp:
                top=stack.pop() if stack else '#'
                if mapp[char]!=top:
                    return False
            else:
                stack.append(char)
        return not stack