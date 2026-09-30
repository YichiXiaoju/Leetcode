def subsets(nums):
    result = []
    path = []
    def backtrack(start):
        result.append(path.copy())

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result

def combine(n, k):
    result = []
    path = []

    def backtrack(start):
        if len(path) == k:
            result.append(path.copy())
            return
        for i in range(start, n+1):
            path.append(i)
            backtrack(i + 1)
            path.pop()

    backtrack(1)
    return result

def permute(nums):
    result = []
    path = []
    def backtrack():
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for num in nums:
            if num in path:
                continue
            path.append(num)
            backtrack()
            path.pop()
    backtrack()
    return result

def combinationSum(candidates, target):
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining < 0:
            return
        if remaining == 0:
            result.append(path.copy())
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i])
            path.pop()
    backtrack(0, target)
    return result

def generateParenthesis(n):
    result = []
    path = []

    def backtrack(left, right):
        if left == 0 and right == 0:
            result.append("".join(path))
            return
        if left < n:
            path.append("(")
            backtrack(left - 1, right)
            path.pop()
        if right < left:
            path.append(")")
            backtrack(left, right - 1)
            path.pop()
    backtrack(0, 0)
    return result
        