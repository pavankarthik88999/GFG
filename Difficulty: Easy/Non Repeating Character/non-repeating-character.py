class Solution:
    def nonRepeatingChar(self,s):
        # code here
        count={}
        for i in s:
                count[i]=count.get(i,0)+1
        for i in s:
            if count[i]==1:
                return i
                break
        return '$'
    