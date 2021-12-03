from typing import List


class Solution:
    def getFirstPositiveIndex(self, nums: List[int]) -> int:
        bad = 0
        good = len(nums)
        mid = good // 2
        while good - bad > 1:
            if nums[mid] > 0:
                good = mid
            else:
                bad = mid
            mid = (good + bad) // 2
        return good

    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]**2]
        result = []
        first_pos = self.getFirstPositiveIndex(nums)
        positives, negatives = nums[first_pos:], nums[:first_pos]
        neg_index, pos_index = len(negatives) - 1, 0
        while 0 <= neg_index and pos_index < len(positives):
            neg_square = negatives[neg_index] ** 2
            pos_square = positives[pos_index] ** 2
            if pos_square < neg_square:
                result.append(pos_square)
                pos_index = pos_index + 1
            else:
                result.append(neg_square)
                neg_index = neg_index - 1
        if 0 <= neg_index:
            for neg in reversed(negatives[:neg_index + 1]):
                result.append(neg**2)
        if pos_index < len(positives):
            for pos in positives[pos_index:]:
                result.append(pos**2)
        return result


numsTest = [1]
print(Solution().sortedSquares(numsTest))
