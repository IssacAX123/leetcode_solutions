from collections import deque

class MovingAverage:
    def __init__(self, period):
        self.period = period
        self.average = 0
        self.period_array = deque()

    def next(self, val):
        if len(self.period_array) < self.period:
            self.period_array.append(val)
            self.average = sum(self.period_array)/len(self.period_array)
        else:
            total = self.average * self.period
            total -= self.period_array.popleft()
            total += val
            self.period_array.append(val)
            self.average = total/self.period

m = MovingAverage(3)
m.next(1)
print(m.period_array, m.average)
m.next(10)
print(m.period_array, m.average)
m.next(3)
print(m.period_array, m.average)
m.next(5)
print(m.period_array, m.average)