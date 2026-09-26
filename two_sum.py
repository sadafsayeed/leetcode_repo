class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:    
        # Time complexity:O(n)
        # Space complexity:O(n)
        h_m = dict()
        i=0
        for num in nums:
            ki = target - num
            if ki in h_m:
                return [i, h_m[ki]]
            h_m[num] = i
            i+=1
