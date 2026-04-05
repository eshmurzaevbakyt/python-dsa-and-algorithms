def topKFrequent(self, nums, k):
    count = {}
    frequence = [[] for i in range(len(nums) + 1)]
    res = []

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        frequence[c].append(n)

    for i in range(len(frequence) - 1, 0, -1):
        for n in frequence[i]:
            res.append(n)
            if len(res) == k:
                return res