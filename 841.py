class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        self.seen = [False] * n

        def dfs(room):
            self.seen[room] = True
            for key in rooms[room]:
                if not self.seen[key]:
                    dfs(key)

        dfs(0)
        return all(self.seen)
