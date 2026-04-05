def twoSum(self, nums, target):
    hashmap = {}
    for i, n in enumerate(nums):
        if target - n in hashmap:
            return [hashmap[target - n], i]
        else:
            hashmap[n] = i
    return