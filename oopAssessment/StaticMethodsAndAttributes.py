class Calculator:
    count = 0  # Static attribute

    @staticmethod
    def add(a, b):
        Calculator.count += 1
        return a + b

print(Calculator.add(5, 3))
print(Calculator.count)