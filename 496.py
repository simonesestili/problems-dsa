class Solution:
    def nextGreaterElement(self, nums1, nums2):
        queries, stack = {}, []
        for num in nums2[::-1]:
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
            if len(stack) > 1:
                queries[stack[-1]] = stack[-2]
        return [-1 if num not in queries else queries[num] for num in nums1]        
