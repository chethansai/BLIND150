DETERMINE PARTITION .L,R  CHANGE FOR BOTH LEFT PARTIION AND RIGHT PARTITION

def search(nums, target):
    i = 0
    j = len(nums) - 1

    while i <= j:
        m = (i + j) // 2

        if nums[m] == target:
            return m

        # Left portion is sorted
        if nums[i] <= nums[m]:
            if nums[i] <= target < nums[m]:
                j = m - 1
            else:
                i = m + 1

        # Right portion is sorted
        else:
            if nums[m] < target <= nums[j]:
                i = m + 1
            else:
                j = m - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

print(search(nums, target))
