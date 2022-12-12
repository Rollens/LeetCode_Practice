
def findOcurrences(text: str, first: str, second: str) -> list[str]:
    tt = text.split()
    output=[]
    for i in range(len(tt)-2):
        if tt[i] == first and tt[i+1] == second:
            output.append(tt[i+2])
    return output

if __name__ == '__main__':
    text = "we we we we will rock you"
    first = "we"
    second = "we"
    print(findOcurrences(text,first,second))