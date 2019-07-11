'''

Given an array representing tower heights, return true if we can get out of the array

'''





def is_hoppable(towers):
    if not towers:
        return False
    height = 0
    target = len(towers)
    for i in range(len(towers)):
        height = max(height, towers[i])
        if target <= height + i:
            return True
        height -= 1
        if height < 0:
            return False
    return True