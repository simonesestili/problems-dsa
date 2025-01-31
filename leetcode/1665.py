class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda task: task[0] - task[1])
        starting = curr = 0
        for actual, minimum in tasks:
            if curr < minimum:
                starting += minimum - curr
                curr += minimum - curr
            curr -= actual
        return starting    
