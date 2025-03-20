def find_pairs(arr:list)->int:
    count=0
    ans=0
    for j in range(len(arr)-1,-1,-1):
        if arr[j]=='g':
            count+=1
        elif arr[j]=='a':
            ans+=count
    return ans
print(find_pairs(['b','a','a','g','d','c','a','g']))
