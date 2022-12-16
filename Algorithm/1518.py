def numWaterBottles(numBottles: int, numExchange: int) -> int:
    canDrink = numBottles
    hold = 0
    while numBottles >= numExchange:
        temp = numBottles//numExchange
        canDrink += temp
        hold = numBottles % numExchange
        numBottles = temp+hold
    return canDrink

if __name__ == '__main__':
    numWaterBottles(9,3)