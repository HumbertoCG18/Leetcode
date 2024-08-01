class Solution:
    def myAtoi(self, s: str) -> int:
        int_max, int_min = (2**31) - 1, -1 * (2**31)
        num , l, sign, idx = 0, len(s), 1 , 0

        while idx < l and s[idx] == ' ':
            idx += 1

        if idx < l and (s[idx] == '+' or s[idx] == '-'):
            sign = -1 if s[idx] == '-' else 1
            idx += 1

        while idx < l and ord(s[idx]) >= ord('0') and ord(s[idx]) <= ord('9'):
            num = num * 10 + int(s[idx])
            idx += 1

        num *= sign
        
        return min(max(num, int_min), int_max)