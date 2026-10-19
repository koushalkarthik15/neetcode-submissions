class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp1=1
        dp2=2
        for i in range(3,n+1):
            curr=dp1+dp2
            dp1=dp2
            dp2=curr
        return dp2
