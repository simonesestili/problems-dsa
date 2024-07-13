class Solution:
    def survivedRobotsHealths(self, pos, health, direction):
        stack = []
        robots = sorted([[p, h, d, i] for i, (p, h, d) in enumerate(zip(pos, health, direction))])

        for p, h, d, i in robots:
            if d == 'R':
                stack.append([p, h, d, i])
                continue
            while stack and stack[-1][2] == 'R':
                if stack[-1][1] < h:
                    stack.pop()
                    h -= 1
                elif stack[-1][1] > h:
                    stack[-1][1] -= 1
                    h = 0
                    break
                else:
                    stack.pop()
                    h = 0
                    break
            if h:
                stack.append([p, h, d, i])

        return [h for p, h, d, i in sorted(stack, key=lambda x: x[3])]
