def sum_of_q_queries(arr: list, queries: list) -> list:
    # Initialize prefix sum and result lists
    prefix_sum = [arr[0]]
    ans_sum = []
    n = len(arr)

    # Build the prefix sum array
    for i in range(1, n):
        prefix_sum.append(prefix_sum[i-1] + arr[i])

    # Process the queries
    for q in queries:
        i, j = q
        if i > j or i < 0 or j >= n:
            raise Exception("Invalid Input")
        ans_sum.append(prefix_sum[j] - (prefix_sum[i-1] if i > 0 else 0))

    return ans_sum

# Example Test
print(sum_of_q_queries([-6, 3, 2, 4, 5, -2, 1, 9], [(1, 4), (3, 6), (1, 5)]))
