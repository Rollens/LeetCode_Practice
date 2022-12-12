def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    else:
        temp = ['']*numRows
        count = 0
        flag = True
        for i in s:
            if count != numRows and count != -1:
                if flag:
                    temp[count]+=i
                    count = count + 1
                else:
                    temp[count] += i
                    count = count -1
            elif count == numRows:
                count -= 2
                flag = False
                temp[count]+=i
                count -= 1
            elif count == -1:
                count += 2
                flag = True
                temp[count]+=i
                count += 1
        return ''.join(temp)

if __name__ == '__main__':
    convert("PAYPALISHIRING",3)