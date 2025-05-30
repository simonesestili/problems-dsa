class Solution:
    def closestMeetingNode(self, edges, a, b):
        acurr, bcurr = [a], [b]
        aseen, bseen = set(), set()

        ans = []
        while acurr or bcurr:
            anxt, bnxt = [], []
            for node in acurr:
                if node in bseen:
                    ans.append(node)
                    continue
                aseen.add(node)
                if edges[node] != -1 and edges[node] not in aseen:
                    anxt.append(edges[node])
            for node in bcurr:
                if node in aseen:
                    ans.append(node)
                    continue
                bseen.add(node)
                if edges[node] != -1 and edges[node] not in bseen:
                    bnxt.append(edges[node])
            acurr, bcurr = anxt, bnxt
            if ans:
                return min(ans)

        return -1
