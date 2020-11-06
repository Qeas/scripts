class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_indexes = {}
        for key, val in enumerate(nums):
            if target - val in nums_indexes:
                return nums_indexes[target - val], key
            else:
                nums_indexes[val] = key

s = Solution()
print s.twoSum([3,2,4], 6)