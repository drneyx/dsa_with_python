
def linear_search(list, target):
    """
    Return position of target
    """
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Item found at ", index)
    else:
        print("Item not found")

