
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data=dict()
        for item in strs:
            temp=[0]*26
            for i in item:
                temp[ord(i)-97]+=1
            temp=tuple(temp)
            if temp in data:
                data[temp].append(item)
            else:
                data[temp]=[item]
        return list(data.values())




        




        
        

        
            
        