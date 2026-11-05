class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        sols={}
        def dfs(amount):
            if amount==0:
                return 0
            if amount in sols:
                return sols[amount]
            res=1e9
            for coin in coins:
                if amount-coin>=0:
                    res=min(res,1+dfs(amount-coin))
            sols[amount]=res
            return res
        sol=dfs(amount)
        return -1 if sol>=1e9 else sol