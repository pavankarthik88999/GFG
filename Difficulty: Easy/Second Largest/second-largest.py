class Solution:
    def getSecondLargest(self, arr):
        # code here
        n=len(arr)
        arr.sort()
        lar=arr[n-1]
        sm=0
        for i in range(len(arr)):
            if arr[i]<lar and arr[i]>sm:
                sm=arr[i]
            
        if sm!=0:
            return sm
        else:
            return -1
        