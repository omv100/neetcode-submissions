class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        it = set()
        for i in nums:
            if i in it:
                return True
            it.add(i)
        return False
        