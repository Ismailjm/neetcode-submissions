class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            assert nums[i]>=-10**9 and nums[i]<=10**9
        num_unique = list(set(nums))
        return  sorted(nums) != sorted(num_unique) 
