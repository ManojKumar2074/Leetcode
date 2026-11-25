class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        ma = 0
        i = 0
        while i<len(nums):
            if nums[i] == 1:
                count += 1
                if count > ma:
                    ma = count
            else:
                count = 0
            i += 1
        return ma