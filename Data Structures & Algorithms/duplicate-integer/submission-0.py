class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]
            if(prev == curr):
                return True
            else:
                continue
        return False

