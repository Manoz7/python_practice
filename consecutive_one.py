
def dec_to_bin(num):
    binArr = []
    
    if num == 0:
        return "0"
    
    while num >0:
        bit = num%2
        binArr.append(str(bit))
        num //= 2
    
    binArr.reverse()
    return "".join(binArr)
    
def max_consecutive_ones(arr):
    count = 0
    max_count = 0
    
    for num in arr:
        if num == '1':
            count +=1
            max_count = max(max_count, count)
        else:
            count = 0
    
    return max_count


if __name__ == '__main__':
    n = int(input().strip())
    
    result = dec_to_bin(n)

    print(max_consecutive_ones(result))