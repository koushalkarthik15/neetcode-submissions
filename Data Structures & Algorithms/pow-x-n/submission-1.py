class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        if x==0:
            return 0
        if n==0:
            return 1
        power=abs(n)
        while power:
            if power&1:
                ans*=x
            x*=x
            power>>=1
        return ans if n>=0 else 1/ans