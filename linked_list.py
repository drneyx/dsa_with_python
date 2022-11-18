class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of elements in list
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count
    
    def add(self, data):
        """
        Adds new Node containing data at head of the list
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    
    def __repr__(self):
        """
         Return a string representaiotns of the list takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is not self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current =  current.next_node