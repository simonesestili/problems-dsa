class Solution:
    def str2tree(self, s):
        jumps, stack = {}, []
        for i, x in enumerate(s):
            if x == '(': stack.append(i)
            if x == ')': jumps[stack.pop()] = i

        def build(left, right):
            if right < left: return None
            num = 0 

            if s[left] == '-': neg = True; left += 1
            else: neg = False

            while left < len(s) and s[left].isdigit():
                num = num * 10 + int(s[left])
                left += 1
            if left >= len(s) or s[left] == ')': return TreeNode(num * (-1 if neg else 1))
            return TreeNode(num * (-1 if neg else 1), build(left + 1, jumps[left] - 1), build(jumps[left] + 2, right - 1))

        return build(0, len(s) - 1)
