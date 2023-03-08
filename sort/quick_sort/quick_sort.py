def partition(nums,left,right):
    i,j = left,right
    while i < j:
        while i<j and nums[j] <= nums[left]:
            j -= 1 #从右边往左边找第一个大于基准数的元素
        while i < j and nums[i] >= nums[left]:
            i += 1 #从左边往右边找第一个小于基准数的元素
        nums[i],nums[j] = nums[j],nums[i]
        #把大于基准数的元素放左边，小于基准数的放右边
    nums[i],nums[left] = nums[left],nums[i]
    #变更基准数
    return i


def quick_sort(nums,left,right):
    if left > right:
        return
    mark = partition(nums,left,right)
    quick_sort(nums,left,mark-1)
    quick_sort(nums,mark+1,right)



arr = [2,4,1,0,3,5]
quick_sort(arr,0,5)
print(arr)