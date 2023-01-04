def digitCount(self, num: str) -> bool:
    for index,digit in enumerate(num):
        if num.count(str(index)) != int(digit):
            return False
    return True

if __name__ == '__main__':
    digitCount("1210")