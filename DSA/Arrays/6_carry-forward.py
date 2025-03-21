def find_min_length_of_min_and_max_element(arr:list)->int:
    n=len(arr)
    if n<=0:
          return -1
    max_elem=max(arr)
    min_elem=min(arr)
    min_id=-1
    max_id=-1
    ans=float('inf')
    if max_elem==min_elem or n==1:
          return 1
    for i in range(n-1,-1,-1):
        if arr[i]==min_elem:
            min_id=i
            if max_id!=-1:
                ans=min(ans, max_id-min_id+1)
        elif arr[i]==max_elem:
            max_id=i
            if min_id!=-1:
                ans=min(ans, max_id-min_id+1)
    return ans if ans != float('inf') else -1
print(find_min_length_of_min_and_max_element([1,2,3,1,3,4,6,4,6,3,5]))
              
    