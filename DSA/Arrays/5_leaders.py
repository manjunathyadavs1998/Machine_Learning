def find_leaders(arr:list)->int:
    n=len(arr)
    if n==0:
        return -1
    curr_leader_count=1
    curr_leader=arr[n-1]
    if n==1:
        return curr_leader_count
    for i in range(n-2,-1, -1):
        if arr[i]>curr_leader:
            curr_leader_count+=1
            curr_leader=arr[i]
    return curr_leader_count
print(find_leaders([15,-1,7,2,5,4,-2,3]))


def find_leaders_elem(arr: list) -> list:
    n = len(arr)
    if n == 0:
        return []
    
    leaders = [arr[-1]]
    curr_leader = arr[-1]

    for i in range(n-2, -1, -1):
        if arr[i] > curr_leader:
            leaders.append(arr[i])
            curr_leader = arr[i]
    
    return leaders[::-1]  

print(find_leaders_elem([15, -1, 7, 2, 5, 4, -2, 3]))  
