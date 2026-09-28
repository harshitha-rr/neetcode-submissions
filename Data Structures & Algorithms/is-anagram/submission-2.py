class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_arr= [0]* 26
        for item in s:
            char_arr[ord(item)-97]+=1
        for item in t:
            char_arr[ord(item)-97]-=1
        for counter in char_arr:
            if counter!=0:
                return False
        return True
