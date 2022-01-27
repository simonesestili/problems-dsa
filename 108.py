class Solution:
    def sortedArrayToBST(self, nums):

        def make_node(left, right):
            if right < left: return None
            mid = (left + right) // 2
            return TreeNode(nums[mid], make_node(left, mid - 1), make_node(mid + 1, right))

        return make_node(0, len(nums) - 1)
