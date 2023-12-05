class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                pos1, pos2 = i + j, i + j + 1
                carry = product + result[pos2]

                result[pos1] += carry // 10
                result[pos2] = carry % 10

        result_str = ""
        for digit in result:
            if not (digit == 0 and len(result_str) == 0):
                result_str += str(digit)

        return result_str if result_str else "0"