class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            pi=self.partition(arr,low,high)
            self.quickSort(arr,low,pi-1)
            self.quickSort(arr,pi+1,high)
    
    # def partition(self, arr, low, high):
    #     pivot = arr[low]
    #     l = low + 1  # Start left pointer after the pivot
    #     r = high     # Start right pointer at the end

        # while l <= r:
        #     while l <= r and arr[l] <= pivot:
        #       l += 1
        #     while l <= r and arr[r] > pivot:
        #         r -= 1
        #     if l <= r:
        #     # Swap arr[l] and arr[r]
        #         arr[l], arr[r] = arr[r], arr[l]
        #         l += 1
        #         r -= 1

        # # Place the pivot in its correct position
        # arr[low], arr[r] = arr[r], arr[low]
        # return r

    
    def partition(self,arr,low,high):
        # code here
        pivot=arr[low]
        l=low+1
        r=high
        while(l<=r):
            while(l<=r and arr[l]<=pivot):
                l+=1
            while(l<=r and arr[r]>pivot):
                r-=1
            if(l<=r):
                t=arr[l]
                arr[l]=arr[r]
                arr[r]=t
                l+=1
                r-=1
        t=arr[r]
        arr[r]=arr[low]
        arr[low]=t
        return r;
