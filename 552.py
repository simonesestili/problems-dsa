class Solution:
    def checkRecord(self, n):
        counts = [1,0,0,0,0,0]
        for _ in range(n):
            next = counts[:]
            next[0] += (counts[1] + counts[2]) % int(1e9 + 7)    
            next[1] += (counts[0] - counts[1]) % int(1e9 + 7)    
            next[2] += (counts[1] - counts[2]) % int(1e9 + 7)    
            next[3] += (counts[0] + counts[1] + counts[2] + counts[4] + counts[5]) % int(1e9 + 7)    
            next[4] += (counts[3] - counts[4]) % int(1e9 + 7)    
            next[5] += (counts[4] - counts[5]) % int(1e9 + 7)    

            counts = next
        return sum(counts) % int(1e9 + 7)    

# class Solution:
#     def checkRecord(self, n):
#         # First digit represents total abscences
#         # Second digit represents current late streak
#         counts = {'00':1, '01':0, '02':0, '10':0, '11':0, '12':0}
#         for _ in range(n):
#             toAdd = {}
#             toAdd['00'] = (counts['01'] + counts['02']) % int(1e9 + 7)
#             toAdd['10'] = (counts['00'] + counts['01'] + counts['02'] + counts['11'] + counts['12']) % int(1e9 + 7)
#             toAdd['01'] = (counts['00'] - counts['01']) % int(1e9 + 7)
#             toAdd['11'] = (counts['10'] - counts['11']) % int(1e9 + 7)
#             toAdd['02'] = (counts['01'] - counts['02']) % int(1e9 + 7)
#             toAdd['12'] = (counts['11'] - counts['12']) % int(1e9 + 7)
#             for key in counts:
#                 counts[key] += toAdd[key]
#         return sum([counts[key] for key in counts]) % int(1e9 + 7)
