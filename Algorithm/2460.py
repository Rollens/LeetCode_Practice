def applyOperations(nums: list[int]) -> list[int]:
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    j = 0
    count = 0
    while j < len(nums):
        if nums[j] == 0:
            nums.pop(j)
            count += 1
            continue
        j += 1
    return nums+[0]*count

if __name__ == '__main__':
    inpt = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
    print(applyOperations(inpt))