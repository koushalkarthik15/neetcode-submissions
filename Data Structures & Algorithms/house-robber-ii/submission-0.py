class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        def dp(start,end):
            dp2=0
            dp1=0
            for i in range(start,end):
                curr=max(dp2+nums[i],dp1)
                dp2=dp1
                dp1=curr
            return dp1
        return max(dp(0,n-1),dp(1,n))