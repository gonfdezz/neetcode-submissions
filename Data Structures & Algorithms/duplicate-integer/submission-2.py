class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsWithoutDupicates = list(set(nums))        
        if len(nums) != len(numsWithoutDupicates):
            return True   
        return False