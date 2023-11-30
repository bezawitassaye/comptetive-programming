class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self.helper(n, 0)

    def helper(self, n: int, power: int) -> bool:
        if n == 0:
            return True
        if n < 0 or power > 14:  # We limit the power to 14 because 3^15 exceeds the input constraints
            return False
        return self.helper(n - 3 ** power, power + 1) or self.helper(n, power + 1)