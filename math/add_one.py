
def add_one(nums):
    
    if nums[-1] != 9:
        nums[-1] += 1
        return nums
    
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == 9 and i != 0:
            nums[i] = 0
            continue
        if i == 0 and nums[i] == 9:
            nums[i] = 0
            nums.insert(0, 1)
            return nums
        else:
            nums[i] += 1
            return nums