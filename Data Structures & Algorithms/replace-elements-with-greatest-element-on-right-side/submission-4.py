class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        x=[]
        y=[]
        for i in range(0,len(arr)-1):
            arr=arr[1:]
            x.append(max(arr))
        x.append(-1)
        return x    
        