class Solution:
    def threeSum(self, nums):
        ans = set()
        pos, neg, zero = [], [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
            else:
                zero.append(num)
        if len(zero) >= 3:
            ans.add((0,0,0))
        p, n = set(pos), set(neg)    
        if zero:
            for num in p:
                if -num in n:
                    ans.add((0, num, -num))
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                if -(pos[i] + pos[j]) in n:
                    ans.add((-(pos[i] + pos[j]), min(pos[i], pos[j]), max(pos[i], pos[j])))
        for i in range(len(neg)):
            for j in range(i + 1, len(neg)):
                if -(neg[i] + neg[j]) in p:
                    ans.add((min(neg[i], neg[j]), max(neg[i], neg[j]), -(neg[i] + neg[j])))
        return [list(a) for a in ans]            
