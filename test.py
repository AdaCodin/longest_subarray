from solution import Solution
import json

class Test:
    def run_tests(self):
        sol = Solution()
        test_cases = [
            ([0, 1], 2),
            ([0, 1, 0], 2),
            ([0, 0, 1, 1, 0], 4),
            ([0, 0, 1, 0, 0, 0, 1, 1], 6),
            ([0, 0, 0], 0),
            ([1, 1, 1], 0),
        ]

        passed = 0
        failed_cases = []

        for i, (nums, expected) in enumerate(test_cases, 1):
            result = sol.findMaxLength(nums)
            if result == expected:
                passed += 1
            else:
                failed_cases.append({
                    "test_case_number": i,
                    "input": nums,
                    "expected": expected,
                    "received": result
                })

        total = len(test_cases)

        print(f"\n{passed}/{total} test cases passed.")

        if failed_cases:
            print("\nFailed Test Cases:")
            for fail in failed_cases:
                print(f"  Test #{fail['test_case_number']} - Input: {fail['input']}")
                print(f"    Expected: {fail['expected']}, Received: {fail['received']}")

        result_summary = (passed, total, failed_cases)
        result_str = json.dumps(result_summary)
        print(f"\n===TEST_RESULT_START===\n{result_str}\n===TEST_RESULT_END===")
        return result_summary


if __name__ == "__main__":
    tester = Test()
    result = tester.run_tests()