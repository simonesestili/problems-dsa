class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        groups = defaultdict(int)
        for ans in answers:
            groups[ans + 1] += 1
        num_rabbits = 0
        for group in groups:
            if groups[group] % group == 0:
                num_rabbits += groups[group]
            else:
                num_rabbits += groups[group] + (group - groups[group] % group)
        return num_rabbits        
