def findMinArrowShots(points: list[list[int]]) -> int:
    points.sort(key=lambda x : x[1])
    result , arrow = 1 , points[0][1]
    for start , end in points:
        if start > arrow:
            arrow = end
            result += 1
    return result

if __name__ == '__main__':
    findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])