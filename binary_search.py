def binary_search(list, target):

    first = 0
    last = len(list) - 1

    while first <= last:

        midpoint = (first + first) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1 
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("Item found at ", index)
    else:
        print("Item not found")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = binary_search(numbers, 12)
ver = verify(result)


result = binary_search(numbers, 1)
ver = verify(result)