nums = [0,0,1,1,1,2,2,3,3,3,4,5,6,7,7,7,8,9]
print(nums)

j = 0
for i in  range(1,len(nums)):
	if nums[i] != nums[j]:
		j+=1
		nums[j] = nums[i]
print(nums,j)

