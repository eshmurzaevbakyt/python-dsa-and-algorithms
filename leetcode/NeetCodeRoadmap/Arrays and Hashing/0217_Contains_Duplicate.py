def containsDuplicate(self, nums: list[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
# Less effective solution
def containsDuplicate2(self, nums: list[int]) -> bool:
    n = len(nums)
    nums.sort()
    for x in range(1, n):
        if nums[x] == nums[x - 1]:
            return True
    return False
