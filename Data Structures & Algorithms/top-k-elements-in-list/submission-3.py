class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}

        for item in nums:
            if item in data:
                data[item] += 1
            else:
                data[item] = 1
        l = sorted(data, key=data.get, reverse=True)

        return l[:k]
       
        
