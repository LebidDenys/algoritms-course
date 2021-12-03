from typing import List


class Solution:
	def sortColors(self, nums: List[int]) -> None:
		if len(nums) <= 1:
			return
		swapped_zeros = 0
		swapped_twos = 0
		index = 0
		while index + swapped_twos < len(nums):
			if nums[index] == 0:
				nums.insert(swapped_zeros, nums.pop(index))
				swapped_zeros = swapped_zeros + 1
				index = index + 1
			elif nums[index] == 2:
				nums.insert(len(nums), nums.pop(index))
				swapped_twos = swapped_twos + 1
			else:
				index = index + 1


test_data = [1,0]
Solution().sortColors(test_data)
print(test_data)
