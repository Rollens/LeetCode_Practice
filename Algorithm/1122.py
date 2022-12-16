def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    cp = arr1[:]
    new = []
    for i in arr2:
        if i in arr1:
            num = cp.count(i)
            cp.sort(key=lambda x : x == i)
            new += cp[len(cp)-num:]
            cp = cp[:len(cp)-num]
    if cp:
        cp.sort()
        return new+cp
    else:
        return new

if __name__ == '__main__':
    a1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
    a2 = [2,42,38,0,43,21]
    relativeSortArray(a1,a2)