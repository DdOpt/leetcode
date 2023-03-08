def insert_sort(nums):
    """ 插入排序 """
    # 外循环：base = nums[1], nums[2], ..., nums[n-1]
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        # 内循环：将 base 插入到左边的正确位置
        while j >= 0 and nums[j] > base:
            nums[j + 1] = nums[j]
            # 1. 将 nums[j] 向右移动一位
            j -= 1
        nums[j + 1] = base
        # 2. 将 base 赋值到正确位置
arr = [2,4,1,0,3,5]
insert_sort(arr)
print(arr)