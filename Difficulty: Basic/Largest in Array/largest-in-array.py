class Solution:
    def largest(self, arr):
        # code here
        count=arr[0]
        for i in range(len(arr)):
            if arr[i]>count:
                count=arr[i]
        return count
        
