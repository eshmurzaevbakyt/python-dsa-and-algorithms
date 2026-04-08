def search(self, nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[l]:
            if nums[mid] < target or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if nums[mid] > target or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1