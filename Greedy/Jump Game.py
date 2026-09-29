from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


# Test
s = Solution()
print(s.canJump([2, 3, 1, 1, 4]))  # True
print(s.canJump([3, 2, 1, 0, 4]))  # False
print(s.canJump([0]))              # True
