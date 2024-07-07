class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        ind=0
        flag=0
        while(i>=1):
            
            if nums[i]>nums[i-1]:
                flag=1
                print("i",i,"i-1",i-1)
                ind=i-1
                break
            i-=1
        print(ind)
        if flag==0:
            nums.reverse()
            return nums
        i=len(nums)-1
        while(i>=ind+1):
            if (nums[i]>nums[ind]):
                t=nums[i]
                nums[i]=nums[ind]
                nums[ind]=t
                break
            i-=1

        l=nums[:ind+1]
        l2=nums[ind+1:]
        l2.reverse()
        nums[:]=l+l2
        return nums

        
