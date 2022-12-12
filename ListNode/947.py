import collections


def removeStones(stones: list[list[int]]) -> int:
    # Create dfs recursive
    def dfs(xo,yo):
        nonlocal visited
        if (xo,yo) not in visited:
            visited.add((xo,yo))
            for y in mapX[xo]:
                dfs(xo,y)
            for x in mapY[yo]:
                dfs(x,yo)
    # Create map by x and by y
    mapX = collections.defaultdict(list)
    mapY = collections.defaultdict(list)
    
    # Create counter for connencted
    connected = 0
    
    # Set for visited
    
    visited = set()
    
    # Create Map
    
    for x,y in stones:
        mapX[x].append(y)
        mapY[y].append(x)
    
    # GO
    
    for x,y in stones:
        if (x,y) not in visited:
            dfs(x,y)
            connected += 1
    
    return len(stones) - connected

if __name__ == '__main__':
    removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])