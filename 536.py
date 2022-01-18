class Solution:
    def str2tree(self, s):
        jumps, stack = {}, []
        for i, x in enumerate(s):
            if x == '(': stack.append(i)
            if x == ')': jumps[stack.pop()] = i

        def build(left, right):
            num = 0
            while s[left].isdigit():
                num = num * 10 + int(s[left])
                left += 1
            return TreeNode(

        return build(0, len(s) - 1)
