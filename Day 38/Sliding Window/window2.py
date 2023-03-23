def max_sum(arr, k):
    maximum = -10
    k_sum, start = 0, 0

    for end in range(len(arr)):
        k_sum += arr[end]

        if end >= k-1:
            if k_sum > maximum:
                maximum = k_sum
            k_sum -= arr[start]
            start += 1
    return maximum


nums = [2, 3, 4, 1, 5]
k = 2

print(max_sum(nums, k))
