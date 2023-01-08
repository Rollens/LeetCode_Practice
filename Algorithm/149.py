def maxPoints(points: list[list[int]]) -> int:
    Scope_Table = {}
    maxpoint = 1
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            x1 , y1 = points[i]
            x2 , y2 = points[j]
            #vertical
            if points[i] == points[j]:
                continue
            elif x1 == x2:
                scope = str(x1)+'f'
            #Others
            else:
                scope = (y2-y1)/(x2-x1)

            if 'f' in str(scope):
                cons = 0
            else:
                cons = y2 - scope*x2

            info = (scope,cons)
            if info in Scope_Table:
                if points[i] not in Scope_Table[info]:
                    Scope_Table[info].append(points[i])
                elif points[j] not in Scope_Table[info]:
                    Scope_Table[info].append(points[j])
            else:
                Scope_Table[info] = [points[i],points[j]]

    for ct in Scope_Table.values():
        maxpoint = max(maxpoint,len(ct))
    return maxpoint

if __name__ == '__main__':
    inpt = [[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]
    print(maxPoints(inpt))
