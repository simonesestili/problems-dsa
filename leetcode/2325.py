class Solution:
    def decodeMessage(self, key, message):
        mappings, curr = {}, ord('a')
        for c in key:
            if c == ' ' or c in mappings: continue
            mappings[c] = chr(curr)
            curr += 1 
        return ''.join(' ' if c == ' ' else mappings[c] for c in message)
