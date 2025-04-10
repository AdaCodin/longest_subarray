from solution import Solution

def run_tests():
    sol = Solution()

    # Test case 1
    nums1 = [0, 1]
    assert sol.findMaxLength(nums1) == 2, f"Failed on input {nums1}"

    # Test case 2
    nums2 = [0, 1, 0]
    assert sol.findMaxLength(nums2) == 2, f"Failed on input {nums2}"

    # Test case 3
    nums3 = [0, 0, 1, 1, 0]
    assert sol.findMaxLength(nums3) == 4, f"Failed on input {nums3}"

    # Test case 4
    nums4 = [0, 0, 1, 0, 0, 0, 1, 1]
    assert sol.findMaxLength(nums4) == 6, f"Failed on input {nums4}"

    # Test case 5 - all 0s
    nums5 = [0, 0, 0]
    assert sol.findMaxLength(nums5) == 0, f"Failed on input {nums5}"

    # Test case 6 - all 1s
    nums6 = [1, 1, 1]
    assert sol.findMaxLength(nums6) == 0, f"Failed on input {nums6}"

    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
