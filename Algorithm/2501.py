def longestSquareStreak(nums: list[int]) -> int:
    nums.sort()
    res = []
    for n in nums:
        temp = []
        while n**2 in nums:
            if n in nums:
                temp.append(nums.pop(nums.index(n)))
            temp.append(nums.pop(nums.index(n**2)))
            n = n ** 2
        res.append(temp)
    return max(res,key=len)


if __name__ == '__main__':
    inpt = [4,3,81,9,6,16,8,2]
    t = longestSquareStreak(inpt)
    print(t)