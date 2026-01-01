from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carrier = 1
        for i in range(len(digits) - 1, -1, -1):
            tmp = digits[i] + carrier
            digits[i] = tmp % 10
            carrier = int(tmp / 10)

        if carrier > 0:
            digits.insert(0, carrier)
        return digits

if __name__ == '__main__':
    solu = Solution().plusOne(digits=[9])
    print(solu)