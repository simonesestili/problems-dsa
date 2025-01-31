class Solution:
    def tree2str(self, root):
        if not root: return ''
        left = f'({self.tree2str(root.left)})' if root.left or root.right else ''
        right = f'({self.tree2str(root.right)})' if root.right else ''
        return f'{root.val}{left}{right}'
