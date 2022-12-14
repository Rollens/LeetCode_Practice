import textwrap
def digitSum(s: str, k: int) -> str:
    while len(s) > k:
        s = helper(s,k)
    return s
    
def helper(s:str,k:int):
    temp = textwrap.wrap(s,width=k)
    hold = ''
    for t in temp:
        su = str(sum(list(map(int,t))))
        hold += su
    return hold

if __name__ == '__main__':
    digitSum("11111222223",3)