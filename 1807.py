class Solution(object):
    def evaluate(self, s, knowledge):
        pairs = {}
        for key, val in knowledge:
            pairs[key] = val
        result = ''
        curr_key, in_key = '', False
        for char in s:
            if char == '(':
                in_key = True
            elif char == ')':
                result += pairs.get(curr_key, '?')
                curr_key, in_key = '', False
            elif in_key:
                curr_key += char
            else:
                result += char
        return result
        
        