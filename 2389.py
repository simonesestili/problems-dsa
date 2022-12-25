class Solution:
    def answerQueries(self, nums, queries):
        nums = list(accumulate(sorted(nums)))
        return [bisect_right(nums, query) for query in queries]
