class Solution:
    def countHomogenous(self, s: str) -> int:
        num_homogenous = 0
        curr_char, curr_count = None, 0
        for char in s:
            if char != curr_char:
                num_homogenous += curr_count * (curr_count + 1) // 2
                curr_count = 0
                curr_char = char
            curr_count += 1
        num_homogenous += curr_count * (curr_count + 1) // 2
        return int(num_homogenous % (1e9 + 7))