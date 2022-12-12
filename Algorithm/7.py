def reverse(x: int) -> int:
    if x > (2**31-1) or x < (-2**31):
        return 0
    else:
        atoi = str(x)
        return int(atoi[::-1]) if atoi[0] != '-' else 0-int(atoi[1:][::-1])

if __name__ == '__main__':
    reverse(1534236469)