class Solution:
    def sumFourDivisors(self, nums):
        def factors(x):
            if int(sqrt(x)) == sqrt(x): return []
            res = [1, x]
            for i in range(2, ceil(sqrt(x))):
                if not x % i:
                    res.append(i)
                    res.append(x // i)
            return res

        total = 0
        for num in nums:
            facts = factors(num)
            total += 0 if len(facts) != 4 else sum(facts)
        return total
