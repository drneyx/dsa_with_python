
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

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = linear_search(numbers, 12)
ver = verify(result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = linear_search(numbers, 7)
ver = verify(result)