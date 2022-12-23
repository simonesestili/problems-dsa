class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        seen = [False] * n

        def dfs(room):
            seen[room] = True
            for key in rooms[room]:
                if seen[key]: continue
                dfs(key)

        dfs(0)
        return all(seen)
