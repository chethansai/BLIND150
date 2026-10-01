def find_minimum(nums):
    left = 0
    right = len(nums) - 1

    while left < right:

        # Already sorted
        if nums[left] < nums[right]:
            return nums[left]

        mid = (left + right) // 2

        # Mid is in the left sorted portion
        if nums[mid] >= nums[left]:
            left = mid + 1

        # Mid is in the right rotated portion
        else:
            right = mid

    return nums[left]


nums = [3, 4, 5, 1, 2]

print(find_minimum(nums))
