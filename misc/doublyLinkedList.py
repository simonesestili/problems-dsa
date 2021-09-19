# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        insert = self.containsNode(node)
        if insert:
            self.remove(node)
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev
            self.head.prev = None
        else:
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev
            self.head.prev = None

    def setTail(self, node):
        insert = self.containsNode(node)
        if insert:
            self.remove(node)
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None

    def insertBefore(self, node, nodeToInsert):
        insert = self.containsNode(nodeToInsert)
        if insert:
            self.remove(nodeToInsert)
        if self.head is node:
            self.head.prev = nodeToInsert
            nodeToInsert.next = self.head
            nodeToInsert.prev = None
            self.head = self.head.prev
            return
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        insert = self.containsNode(nodeToInsert)
        if insert:
            self.remove(nodeToInsert)
        if self.tail is node:
            self.tail.next = nodeToInsert
            nodeToInsert.prev = self.tail
            nodeToInsert.next = None
            self.tail = self.tail.next
            return
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            nodeToInsert.next = self.head
            self.head.prev = nodeToInsert
            self.head = self.head.prev
            return
        curr = self.head
        while curr and position != 1:
            curr = curr.next
            position -= 1
        if curr:
            curr.prev.next = nodeToInsert
            nodeToInsert.prev = curr.prev
            curr.prev = nodeToInsert
            nodeToInsert.next = curr

    def removeNodesWithValue(self, value):
        if not self.head:
            return
        # Trim head
        while self.head and self.head.val == value:
            self.head = self.head.next
        # Trim tail
        while self.tail and self.tail.val == value:
            self.tail = self.tail.prev
        curr = self.head
        while curr:
            if curr.val == value:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            curr = curr.next
        
    def remove(self, node):
        if self.head is node:
            self.head = self.head.next
        elif self.tail is node:
            self.tail = self.tail.prev
        else:
            curr = self.head
            while curr:
                if curr is node:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    return
                curr = curr.next

    def containsNodeWithValue(self, value):
        curr = self.head
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False

    def containsNode(self, node):
        curr = self.head
        while curr:
            if curr is node:
                return curr
            curr = curr.next
        return None    
