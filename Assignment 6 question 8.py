class SumToZero:
    def __init__(self, numbers):
        self.numbers = numbers

    def find_elements(self):
        self.numbers.sort()
        result = []
        for i in range(len(self.numbers)-2):
            if i > 0 and self.numbers[i] == self.numbers[i-1]:
                continue
            l, r = i+1, len(self.numbers)-1
            while l < r:
                current_sum = self.numbers[i] + self.numbers[l] + self.numbers[r]
                if current_sum == 0:
                    result.append([self.numbers[i], self.numbers[l], self.numbers[r]])
                    while l < r and self.numbers[l] == self.numbers[l+1]:
                        l += 1
                    while l < r and self.numbers[r] == self.numbers[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    r -= 1
        return result

numbers = [-25, -10, -7, -3, 2, 4, 8, 10]
result = SumToZero(numbers).find_elements()
print(result)
# [[-10, 2, 8], [-7, -3, 10]]
