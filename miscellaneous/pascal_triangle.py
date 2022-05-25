def get_row(row_index):
    if row_index == 0:
        return [1]
    rows = 1
    result = [1,1]
    while rows < row_index:
        temp = [1]
        for i in range(rows):
            temp.append(result[i] + result[i+1])
        rows += 1
        temp.append(1)
        result = temp
    return result


print(get_row(int(input())))
