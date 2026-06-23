def sortColors(nums):
    i = 0
    k =0
    j = len(nums)-1
    while(k<=j):
        if nums[k]==1:
                k+=1
        elif nums[k]==2:
                nums[k], nums[j]= nums[j],nums[k]
                j-=1
        else:
            nums[k],nums[i] = nums[i], nums[k]
            i+=1
            k+=1