def singleNumber(self, nums: list[int]) -> list[int]:
    from collections import Counter
    ct = Counter(nums)
    return [ x for x,_ in ct.most_common()[::-1][:2]]