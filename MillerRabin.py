import random

class MillerRabin():
    # 初始化待求数值n和测试轮次k
    def __init__(self, n, k) -> None:
        self.n = n
        self.k = k
        self.s = 0
        self.d = self.n - 1
        # 根据输入的n求解s和d
        while self.d % 2 == 0:
            self.s += 1
            self.d = self.d // 2

    # 执行k轮Miller-Rabin测试
    def function(self):
        for i in range(self.k):
            a = random.randint(2, self.n - 2) # 随机初始化基
            x = a**self.d % self.n
            for j in range(self.s):
                y = x**2 % self.n #遍历r \in [1,s)，并对其模进行检验
                if y == 1 and x != 1 and x != self.n - 1:
                    return  "composite"
                x = y
            if y != 1:
                return "composite"
        return "probably prime"