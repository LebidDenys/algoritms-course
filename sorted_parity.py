from typing import List


class Solution:
	def sortArrayByParity(self, A: List[int]) -> List[int]:
		odd_arr = []
		even_arr = []
		for num in A:
			if num & 1:
				odd_arr.append(num)
			else:
				even_arr.append(num)

		return even_arr + odd_arr


res = Solution().sortArrayByParity([3, 1, 2, 4])
print(res)
