class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, path, path_sum):
            if path_sum == target:
                res.append(path.copy())
                return

            for j in range(start, len(candidates)):
                if j > start and candidates[j] == candidates[j - 1]:
                    continue

                if path_sum + candidates[j] > target:
                    break

                path.append(candidates[j])
                dfs(j + 1, path, path_sum + candidates[j])
                path.pop()

        dfs(0, [], 0)
        return res