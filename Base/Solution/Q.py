class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


class MaxLimitCalculator(Calculator):
    def maxLimit(self):
        if self.value > 100:
            self.value = 0
            return self.value
        else:
            return self.value


cal = MaxLimitCalculator()
cal.add(10)
cal.add(90)
cal.add(2)

print(cal.value)
