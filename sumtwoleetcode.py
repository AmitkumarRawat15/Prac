def sum(nums, target):
    d = {}
    for i, j in enumerate(nums):
        r = target - j
        if r in d: 
            return [d[r], i]
        d[j] = i
        print(d)
		
		# An Upvote will be encouraging

nums = [2,5,5,11]
target = 10
print(sum(nums, target))