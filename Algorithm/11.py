def maxArea(self, height: list[int]) -> int:
    left = 0
    right = len(height)-1
    water = 0
    while left < right:
        water = max(water,(right-left)*min(height[left],height[right]))
        if height[left] > height[right]:
            right -= 1
        elif height[left] < height[right]:
            left += 1
        else:
            left += 1
            right -= 1
    return water