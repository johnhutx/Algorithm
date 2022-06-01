import random


# 返回[0,1)的一个小数
# 任意的x，x谁与[0,1)，[0,x)范围上的数出现概率有 x -> x^2
def xToPower2():
    return max(random.random(), random.random())


class RandToRand:
    def __init__(self):
        pass

    # 从整数1-5随机到1-7随机
    @staticmethod
    def rand1To5():
        return int(random.random() * 5 + 1)

    # 等概率得到0和1
    def prob_0_1(self):
        while True:
            num = self.rand1To5()
            if num != 3:
                break

        if num == 1 or num == 2:
            return 0
        elif num == 4 or num == 5:
            return 1

    # 等概率返回0~7
    def rand000To111(self):
        return (self.prob_0_1() << 2) + (self.prob_0_1() << 1) + self.prob_0_1()

    # 等概率返回1~7
    def rand1To7(self):
        while True:
            num = self.rand000To111()
            if num != 7:
                break
        return num + 1


if __name__ == '__main__':
    print("Testing starts:")
    # random.random() -> double -> [0,1)
    testTimes = 1000000
    count = 0
    for i in range(testTimes):
        # [0,1) 等概率返回
        if random.random() < 0.3:
            count += 1
    print(float(count / testTimes))
    print("========================")

    # [0,1) -> [0,8)
    count = 0
    for i in range(testTimes):
        if random.random() * 8 < 5:
            count += 1
    print(count / testTimes)
    print(5/8)
    print("========================")

    count = 0
    x = 0.17
    for i in range(testTimes):
        if xToPower2() < x:
            count += 1
    print(count/testTimes)
    print(x**2)
    print("========================")

    # 等概率返回1~7
    count = 0
    rand = RandToRand()
    for i in range(testTimes):
        if rand.rand1To7() == 1:
            count += 1
    print(count/testTimes)
    print(1/7)