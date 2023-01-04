def kLengthApart(nums: list[int], k: int) -> bool:
    counter = 0
    first = nums.index(1)
    nums = nums[first:]
    for n in nums[1:]:
        if not n:
            counter += 1
        else:
            if counter < k:
                return False
            else:
                counter = 0
    return True

if __name__ == '__main__':
    kLengthApart([1,0,0,0,1,0,0,1],2)