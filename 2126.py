class Solution:
    def asteroidsDestroyed(self, mass, arr):
        for weight in sorted(arr):
            if mass < weight: return False
            mass += weight
        return True
