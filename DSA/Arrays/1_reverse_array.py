def reverse_array(arr: list, startIndex: int, lastIndex: int) -> list:
    while startIndex < lastIndex:
        arr[startIndex], arr[lastIndex] = arr[lastIndex], arr[startIndex]
        startIndex += 1
        lastIndex -= 1
    return arr

def reverse_array_by_k(arr,k)->list:
    n=len(arr)
    k=k%n
    reverse_array(arr,0,n-1)
    reverse_array(arr,0,k-1)
    reverse_array(arr,k,n-1)
    return arr
print(reverse_array([1,2,3,4,5,6,7,8,9],0,8))
print(reverse_array_by_k([1,2,3,4,5,6,7,8,9,10],10))
    