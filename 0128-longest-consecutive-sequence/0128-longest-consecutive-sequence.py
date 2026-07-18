class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])
        for j in hashset:
            if j - 1 not in hashset:
                current_num = j
                current_streak = 1
                while current_num + 1 in hashset:
                    current_num += 1
                    current_streak += 1
                count = max(count, current_streak)
        return count