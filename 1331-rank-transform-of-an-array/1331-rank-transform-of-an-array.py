class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # 1. Get the unique elements in sorted order
        sorted_unique = sorted(list(set(arr)))
        
        # 2. Map each element to its rank (starting from 1)
        rank_map = {}
        for rank, val in enumerate(sorted_unique, 1):
            rank_map[val] = rank
            
        # 3. Replace each element in the original array with its rank
        return [rank_map[x] for x in arr]