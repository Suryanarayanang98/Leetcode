class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        desc_flag = True
        print(nums)
        for i in range(len(nums)-1,0,-1):
            print(i)
            if nums[i-1]<nums[i]:
                print(f"{i} here")
                desc_flag = False
                break
        
        if desc_flag:
            k = 0
        else:  
            j = len(nums)-1
            while j>=i:
                if nums[i-1]<nums[j]:
                    print(f"{j} here")
                    break
                j-=1
            nums[i-1],nums[j] = nums[j],nums[i-1]
            k = i

        print(nums,k)
        print('sorting')
        sort_flag = True
        while sort_flag:
            sort_flag = False
            for n in range(k,len(nums)-1):
                if nums[n] > nums[n+1]:
                    nums[n],nums[n+1] = nums[n+1],nums[n]
                    sort_flag = True
            print(nums)