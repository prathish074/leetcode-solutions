class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(start, path, total):
            # Base case: if total == target, add combination
            if total == target:
                res.append(list(path))
                return
            # If total > target, stop exploring
            if total > target:
                return

            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # can reuse same element
                path.pop()  # undo

        backtrack(0, [], 0)
        return res
