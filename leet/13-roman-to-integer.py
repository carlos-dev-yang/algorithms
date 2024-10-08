from lib.leetcode_tester import run_tests

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total=0
        prev_value=0
        for char in reversed(s):
            print(char)
            curr_value = roman_values[char]
            if curr_value >= prev_value:
                total += curr_value
            else:
                total -= curr_value
            prev_value = curr_value
        return total
          
if __name__ == "__main__":
    solution = Solution()
    
    roman_test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994)
    ]
    
    print("Roman to Integer 테스트 실행:")
    run_tests(solution.romanToInt, roman_test_cases)


"""

"""