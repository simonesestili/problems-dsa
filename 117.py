class Solution:
    def connect(self, root):
        
        conn = root
        while conn:
            dummy = curr = Node()
            while conn:
                if conn.left:
                    curr.next = conn.left
                    curr = curr.next
                if conn.right:
                    curr.next = conn.right
                    curr = curr.next
                conn = conn.next
            conn = dummy.next

        return root
