# Reverse an array using two-pointer approach

def rev_arr(arr):
    
    left=0
    right= len(arr) -1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr

if __name__ == "__main__":

    arr = [1, 4, 5, 6, 7]

    rever_array = rev_arr(arr)

    print(rever_array)

    for re in rever_array:
        print(re, end=' ')

    new_arr = [2,3,5,2,34]
    print()
    new_arr.reverse()
    print(new_arr)

    new_arr = [2, 33, 45, 22, 34]
    print(new_arr[::-1])