class Solution:
    def ladderLength(self, start, end, words):
        n, edges = len(start), defaultdict(set)
        for word in words:
            for i in range(n):
                edges[word[:i] + '*' + word[i+1:]].add(word)

        queue, seen = deque([(start, 1)]), set([start])
        while queue:
            word, dist = queue.popleft()
            if word == end: return dist
            for i in range(n):
                for j in edges[word[:i] + '*' + word[i+1:]]:
                    if j not in seen:
                        queue.append((j, dist + 1))
                        seen.add(j)
        return 0
            
