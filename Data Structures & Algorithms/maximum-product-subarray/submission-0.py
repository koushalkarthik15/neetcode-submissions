class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curmax=1
        curmin=1
        for num in nums:
            temp=curmax*num
            curmax=max(num*curmax,num*curmin,num)
            curmin=min(num*curmin,num,temp)
            res=max(res,curmax)
        return res