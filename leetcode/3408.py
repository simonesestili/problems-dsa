class TaskManager:
    def __init__(self, tasks):
        self.h = []
        self.tasks = {}
        for u, i, p in tasks:
            heappush(self.h, (-p, -i, u))
            self.tasks[i] = (u, p)

    def add(self, user, task, priority):
        self.tasks[task] = (user, priority)
        heappush(self.h, (-priority, -task, user))

    def edit(self, task, priority):
        u, p = self.tasks[task]
        self.add(u, task, priority)

    def rmv(self, task):
        self.tasks[task] = (-1, -1)

    def execTop(self):
        while self.h:
            p, i, u = heappop(self.h)
            if self.tasks[-i] == (u, -p):
                self.rmv(-i)
                return u
        return -1
