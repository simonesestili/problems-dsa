import enum
class Solution:
    def minCameraCover(self, root):
        self.cameras = 0
        
        def dfs(node):
            if node is None: return States.MONITORED_NOCAM
            left, right = dfs(node.left), dfs(node.right)
            if States.UNMONITORED in (left, right):
                self.cameras += 1
                return States.HAS_CAMERA
            if States.HAS_CAMERA in (left, right):
                return States.MONITORED_NOCAM
            return States.UNMONITORED

        return int(dfs(root) == States.UNMONITORED) + self.cameras

class States(enum.Enum):
    HAS_CAMERA = 1
    MONITORED_NOCAM = 2
    UNMONITORED = 3
