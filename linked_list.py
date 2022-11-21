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
    

    def search(self, key):
        """
        Seach for the first node containing the data matches the key

        runs in O(n)
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    

    def insert(self, data, index):
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            prev = current
            next = current.next_node

            prev.next_node = new
            new.next_node = next


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
        return '-> '.join(nodes)



def cube_num(nums):
    for i in nums:
        yield(i*i*i)

num_set = cube_num([1,2,3,4,5])
res = num_set


nums = [2,7,11,15]
target=9
d={}

for i in range(len(nums)):
    if(target-nums[i] in d):
        print([d[target-nums[i]], i])
    else:
        d[nums[1]]=i


def Taple(tuple, t):
    val = 0
    
    for tup in tuple:
        if (tup == t):
            val += 1
    print(val)
    print(tuple)

tuple = (1,1,2,2,5)