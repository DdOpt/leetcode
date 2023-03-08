def merge(nums,left,mid,right):
    tmp = nums[left:right+1]
    left_start,left_end = left-left,mid-left
    right_start,right_end = mid -left + 1,right-left
    i,j = left_start,right_start
    for k in range(left,right + 1):
        #如果左子数组已经合并完毕，取右子数组
        if i > left_end:
            nums[k] = tmp[j]
            j += 1
        #如果右子数组已经合并完毕，或者左子数组元素 <= 右子数组元素，
        #取左子数组元素
        elif j > right_end or tmp[i] <= tmp[j]:
            nums[k] = tmp[i]
            i += 1
        #左右子数组元素都未合并完且左子数组元素 > 右子数组元素，
        #取右子数组元素
        else:
            nums[k] = tmp[j]
            j += 1
def merge_sort(nums,left,right):
    if left >= right:
        return
    mid = (left+right)//2
    merge_sort(nums,left,mid)
    merge_sort(nums,mid+1,right)
    merge(nums,left,mid,right)

arr = [2,4,1,0,3,5]
merge_sort(arr,0,len(arr)-1)
print(arr)