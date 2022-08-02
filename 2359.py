class Solution:
    def closestMeetingNode(self, edges, a, b):
        alevel, blevel = [a], [b]
        aseen, bseen = set(), set()
        works = []
        while alevel or blevel:
            nxt_alevel = []
            nxt_blevel = []
            for node in alevel:
                if node in bseen:
                    works.append(node)
                    continue
                aseen.add(node)
                if edges[node] != -1 and edges[node] not in aseen:
                    nxt_alevel.append(edges[node])
            alevel = nxt_alevel
            for node in blevel:
                if node in aseen:
                    works.append(node)
                    continue
                bseen.add(node)
                if edges[node] != -1 and edges[node] not in bseen:
                    nxt_blevel.append(edges[node])
            blevel = nxt_blevel
            if works: break
        return -1 if not works else min(works)
