class Solution:
    def isPossibleDivide(self, nums, k):
        n, count = len(nums), Counter(nums)
        if n % k: return False

        for num in sorted(count.keys()):
            if count[num-1] > 0 or count[num] == 0: continue
            c = count[num]
            for x in range(num, num + k):
                if count[x] < c: return False
                count[x] -= c

        return not any(count[num] != 0 for num in count)
