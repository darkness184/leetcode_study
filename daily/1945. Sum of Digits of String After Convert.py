"""
The terget of this function is to calculate sum of letters in a string after convert it to a number in alphabet

condition:
- format the string to remove the spaces
- convert the string to a number based on the alphabet
- sum the digits of the number with k times

solution:
1. remove the spaces from the string
2. convert the string to a number based on the alphabet
3. sum the digits of the number with k times
4. return the result

note:
"""


class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        string_format = s.strip().replace(" ","")
        num_str = ''.join([str(ord(char) - 96) for char in string_format])

        for _ in range(0,k):
            num_str = str(sum(int(num) for num in num_str))

        return int(num_str)