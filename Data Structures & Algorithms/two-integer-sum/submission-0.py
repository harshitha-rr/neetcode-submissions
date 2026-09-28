class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data={}
        for x, n in enumerate(nums):
            if (target-n) in data:
                return [data[target-n],x]
            data[n]=x
        
            
        