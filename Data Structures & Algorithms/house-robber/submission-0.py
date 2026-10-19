class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp2=nums[0]
        dp1=max(nums[0],nums[1])
        for i in range(2,n):
            curr1,curr2=dp2+nums[i],dp1
            curr=max(curr1,curr2)
            dp2=dp1
            dp1=curr
        return dp1