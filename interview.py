
class Store:

    def __init__(self):
        self.values = []
        self.map = defaultdict(list)
    

    def insertItem(self, item):
        """
        Function to insert a new item into the store
        """
        self.values.append(item)
        self.map[item].add(len(self.values) - 1)


    def removeItem(self, item):
        """
        Function to remove an item into the store
        """

        return