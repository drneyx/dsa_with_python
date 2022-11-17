def recursive_binary_search(list, target):
   
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2

        if midpoint == target:
            return True
        elif midpoint < target:
            return recursive_binary_search(list[midpoint+1:], target)
        else:
            return recursive_binary_search(list[:midpoint], target)