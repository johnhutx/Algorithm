class PreSum:
    def __init__(self, arr):
        self.arr = arr
        self.preSum = [] * len(self.arr)

    # RangeSum, sum arr from pos 0 to i
    def range_sum_1(self, L, R):
        pre_sum = 0
        for i in range(L, R + 1):
            pre_sum += self.arr[i]
        return pre_sum

    def range_sum_2(self):
        N = len(self.arr)
        self.preSum[0] = self.arr[0]
        for i in range(1, N):
            self.preSum[i] = self.preSum[i - 1] + self.arr[i]

    # def range_sum(self, L, R):


if __name__ == '__main__':
    pass
