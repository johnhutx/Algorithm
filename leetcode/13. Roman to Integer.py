# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

"""
Approach 1: Left-to-Right Pass

total = 0
i = 0
while i < s.length:
    if at least 2 symbols remaining AND value of s[i] < value of s[i + 1]:
        total = total + (value of s[i + 1]) - (value of s[i])
        i = i + 2
    else:
        total = total + (value of s[i])
        i = i + 1
return total

======================================================================================================
Approach 2: Left-to-Right Pass Improved

total = 0
i = 0
while i < s.length:
    if at least 2 characters remaining and s.substing(i, i + 1) is in values:
        total = total + (value of s.substring(i, i + 1))
        i = i + 2
    else:
        total = total + (value of s[i])
        i = i + 1
return total

======================================================================================================
Approach 3: Right-to-Left Pass

last = s.length - 1
total = value(last)
`
for i from last - 1 down to 0:
    if value(s[i]) < value(s[i+1]):
        total -= value(s[i])
    else:
        total += value(s[i])
return sum
"""

values = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


class Solution:
    # Approach 2: Left-to-Right Pass
    # Time complexity: O(1), space complexity O(1)
    def romanToInt_1(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
                total = total + values[s[i+1]] - values[s[i]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total

    # Approach 2: Left-to-Right Pass with 2 symbols included in the hash table
    # Time complexity: O(1), space complexity O(1)
    def romanToInt_2(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in values:
                total += values[s[i:i+2]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total

    # Approach 3: Right-to-Left Pass
    # Time complexity: O(1), space complexity O(1)
    def romanToInt_3(self, s: str) -> int:
        total = values[s[-1]]
        for i in reversed(range(len(s)-1)):
            if values[s[i+1]] > values[s[i]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
