class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        def bt(i,subset):
            if i==len(nums):
                res.add(tuple(subset))
                return
            subset.append(nums[i])
            bt(i+1,subset)
            subset.pop()
            bt(i+1,subset)
        nums.sort()
        bt(0,[])
        return [list(s) for s in res]