class Arithmetic:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


# 상속
class MoreArithmetic(Arithmetic):
    def pow(self):
        result = self.first ** self.second
        return result


# 나누기 안정화
class SafeArithmetic(Arithmetic):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = Arithmetic(3, 4)
print(type(a))
print('=' * 100)
print(a.first)
print(a.second)
