class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3

        leftcurr, leftvals = sum(nums[:n]), [-x for x in nums[:n]]
        heapify(leftvals)
        leftmns = [leftcurr]
        for i in range(n):
            if -leftvals[0] > nums[n+i]:
                leftcurr -= -heapreplace(leftvals, -nums[n+i])
                leftcurr += nums[n+i]
            leftmns.append(leftcurr)

        rightcurr, rightvals = sum(nums[2*n:]), nums[2*n:]
        heapify(rightvals)
        ans = leftmns[-1] - rightcurr
        for i in range(n):
            if rightvals[0] < nums[2*n-1-i]:
                rightcurr -= heapreplace(rightvals, nums[2*n-1-i])
                rightcurr += nums[2*n-1-i]
            ans = min(ans, leftmns[-2-i] - rightcurr)

        return ans
