from typing import List


class Solution:
	def getFirstPositiveIndex(self, nums: List[int]) -> int:
		bad = 0
		good = len(nums)
		mid = good // 2
		while good - bad > 1:
			if nums[mid] >= 0:
				good = mid
			else:
				bad = mid
			mid = (good + bad) // 2
		return good

	def sortedSquares(self, nums: List[int]) -> List[int]:
		if len(nums) == 1:
			return [nums[0] ** 2]
		result = []
		first_positive = self.getFirstPositiveIndex(nums)
		neg_index, pos_index = first_positive - 1, first_positive
		while 0 <= neg_index and pos_index < len(nums):
			neg_value_abs = abs(nums[neg_index])
			pos_value_abs = abs(nums[pos_index])
			if neg_value_abs > pos_value_abs:
				result.append(pos_value_abs ** 2)
				pos_index = pos_index + 1
			else:
				result.append(neg_value_abs ** 2)
				neg_index = neg_index - 1
		if 0 <= neg_index:
			for neg in reversed(range(neg_index + 1)):
				result.append(nums[neg] ** 2)
		if pos_index < len(nums):
			for pos in range(pos_index, len(nums)):
				result.append(nums[pos] ** 2)
		return result


numsTest = [-1,0,3]
print(Solution().sortedSquares(numsTest))
