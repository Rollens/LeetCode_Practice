class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        m = abs(min(nums,key=abs))
        return m if m in nums else 0-m