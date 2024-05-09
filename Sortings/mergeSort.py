class Solution:
    def merge(self,arr, l, mid, h): 
        # code here
        temp=[]
        left=l
        right=mid+1
        
        while(left<=mid and right<=h):
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while(left<=mid):
            temp.append(arr[left])
            left+=1
        while(right<=h):
            temp.append(arr[right])
            right+=1
        for i in range(l,h+1):
            arr[i]=temp[i-l]
        return arr
                
    def mergeSort(self,arr, l, r):
        #code here
        if l>=r:
            return
        mid=(l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)

