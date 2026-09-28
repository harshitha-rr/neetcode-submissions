class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup={}
        for item in nums:
            if item in dup:
                dup[item]+=1
            else:
                dup[item]=1
        for val in dup.values():
            if val>=2:
                return True
        return False

