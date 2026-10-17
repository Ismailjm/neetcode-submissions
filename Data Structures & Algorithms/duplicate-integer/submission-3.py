class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        assert len(nums)>=0 and len(nums) <= 10**5
        for i in range(len(nums)):
            assert nums[i]>=-10**9 and nums[i]<=10**9
        num_unique = list(set(nums))
        if sorted(nums) == sorted(num_unique) : 
            return False
        return True
        


# nums=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20]

# print(sorted(set(nums)))