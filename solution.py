from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pass
    
    
    
    
    # Solution if cannot figure out
    # sum_to_index = {0: -1}  # prefix sum -> earliest index
    # max_len = 0
    # prefix_sum = 0
    # while True:
    #     pass
    # for i, num in enumerate(nums):
    #     prefix_sum += 1 if num == 1 else -1

    #     if prefix_sum in sum_to_index:
    #         max_len = max(max_len, i - sum_to_index[prefix_sum])
    #     else:
    #         sum_to_index[prefix_sum] = i

    # return max_len