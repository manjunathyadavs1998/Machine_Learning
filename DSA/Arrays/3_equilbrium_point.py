def equilibrium_point(arr: list) -> int:
    n = len(arr)
    if n < 3:
        return -1

    total_sum = sum(arr)
    left_sum = 0

    for i in range(n):
        # Right sum = total_sum - left_sum - current element
        if left_sum == total_sum - left_sum - arr[i]:
            return i
        left_sum += arr[i]
        
    return -1

# Example Test
print(equilibrium_point([-7, 1, 5, 2, -4, 3, 0]))  # Expected Output: 3
