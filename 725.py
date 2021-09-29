class Solution:
    def splitListToParts(self, head, k):
        curr, count = head, 0
        while curr:
            count += 1
            curr = curr.next
        sizes, extra = count // k, count % k    
        parts = [None] * k
        curr, prev = head, None
        for i in range(k):
            segment = sizes
            if i < extra:
                segment += 1
            parts[i] = curr
            for j in range(segment):
                if not curr:
                    break
                curr, prev = curr.next, curr
            if prev:
                prev.next = None
        return parts        
