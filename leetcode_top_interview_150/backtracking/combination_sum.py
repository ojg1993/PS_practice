class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(picked, tot, candi):
            if tot == target:
                res.append(picked.copy())
                return

            for i, num in enumerate(candi):
                if tot + num > target:
                    break
                picked.append(num)
                backtrack(picked, tot + num, candi[i:])
                picked.pop()

        candidates.sort()
        res = []
        backtrack([], 0, candidates)
        return res
