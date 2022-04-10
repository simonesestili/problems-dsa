class Solution:
    def maxDiff(self, num):

        def maximize(val):
            for d in val:
                if d != '9':
                    return int(val.replace(d, '9'))
            return int(val)

        def minimize(val):
            for d in val:
                if d != '0' and val[0] != d:
                    return int(val.replace(d, '0'))
                if d not in '01':
                    return int(val.replace(d, '1'))
            return int(val)

        return maximize(str(num)) - minimize(str(num))
