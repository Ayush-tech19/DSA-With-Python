def threesum(nums):
    ans=[]
    n = len(nums)
    for k in range(0,len(nums)-2):
        if k>0 and nums[k]==nums[k-1]:
            k+=1
            continue
        i=k+1
        j=n-1
        while(i<j):
            total = nums[i]+nums[j]+nums[k]
            if total<0:
                i+=1
            elif total>0:
                j-=1
            else:
                ans.append([nums[i],nums[j],nums[k]])
                i+=1
                j-=1
                while(i<j and nums[i]==nums[i-1]):
                    i+=1
                    continue
                while(i<j and nums[j]==nums[j+1]):
                    j-=1
                    continue
    return ans

print(threesum([-1,-1,0,1,1,2,3,3]))

    

         
        

           
