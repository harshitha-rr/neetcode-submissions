class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res={}
        res2={}
        for index in s:
            if index in res:
                res[index]+=1
            else:
                res[index]=1
        for index in t:
            if index in res2:
                res2[index]+=1
            else:
                res2[index]=1
        return res==res2
