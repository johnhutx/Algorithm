# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

"""
# Approach 1: Greedy

define function to_roman(integer):
    roman_numeral = ""
    for each symbol from largest to smallest:
        if value of symbol is greater than integer:
            continue
        symbol_count = number of times symbol value fits into integer
        repeat symbol_count times:
            roman_numeral = concat roman_numeral and symbol
        integer = integer - (value of symbol * symbol_count)

    return roman_numeral

===================================================================================================
"""
class Solution:
    # Greedy approach
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                  (5, "V"), (4, "IV"), (1, "I")]

        roman_digits = []
        for value, symbol in digits:
            if num == 0:
                break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)