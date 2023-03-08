def bubble(nums):
    for i in range(len(nums)):
        for j in range(0,len(nums)-1-i):
            #一次外循环后，后边就可以固定一个元素
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                #把大的元素往后边放
arr = [2,4,1,0,3,5]
bubble(arr)
print(arr)