class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_value = 0
        previous_value = 0

        
        for char in reversed(s):
            current_value = roman_map[char]
            if current_value < previous_value:
                integer_value -= current_value
            else:
                integer_value += current_value
            previous_value = current_value
        
        return integer_value


solution = Solution()
print(solution.romanToInt("III"))       
print(solution.romanToInt("LVIII"))     
print(solution.romanToInt("MCMXCIV"))   
