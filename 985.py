class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum([num for num in nums if num % 2 == 0])
        answer = []
        for query in queries:
            val, idx = query
            if nums[idx] % 2 == 0:
                if val % 2 == 0:
                    even_sum += val
                else:
                    even_sum -= nums[idx]
            else:
                if val % 2 == 1:
                    even_sum += nums[idx] + val
            nums[idx] += val
            answer.append(even_sum)
        return answer

