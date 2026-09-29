from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])

        return res


# Test
s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
print(s.merge([[1, 4], [4, 5]]))                     # [[1,5]]
print(s.merge([[1, 4], [0, 4]]))                     # [[0,4]]
print(s.merge([[1, 4], [2, 3]]))                     # [[1,4]]
