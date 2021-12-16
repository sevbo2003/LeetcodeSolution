"""https://leetcode.com/problems/two-sum/"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for ind, i in enumerate(nums):
                for ind2, a in enumerate(nums):
                    if i + a == target and ind != ind2:
                        return [ind, ind2]


# --> :)
