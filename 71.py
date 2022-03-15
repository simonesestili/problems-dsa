class Solution:
    def simplifyPath(self, path):
        stack = []

        for txt in path.split('/'):
            if txt == '..' and stack:
                stack.pop()
            elif txt and txt != '.' and txt != '..':
                stack.append(txt)

        return '/' + '/'.join(txt for txt in stack)

