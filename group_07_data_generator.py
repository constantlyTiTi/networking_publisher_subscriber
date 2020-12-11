import matplotlib.pyplot as plt
import random,collections

class mimicData:
    def __init__(self,maxTemperature,minTemperature):
        self.MIN_GENERATOR2_RANGE=0
        self.MAX_GENERATOR2_RANGE=100
        self.GENERATOR2_SCALE_FACTOR=1000
        self.GENERATOR3_GAUSS_MEAN=2
        self.GENERATOR3_GAUSS_SD=1
        self.NUMBER_OF_VALUES=3000
        self.value=0
        self.increment_base=19.5
        self.MAX_TEMPERATURE = maxTemperature
        self.MIN_TEMPERATURE = minTemperature
        self.data=collections.deque()
    
    def generator_2(self):
        self.value=float(random.randrange(self.MIN_GENERATOR2_RANGE,self.MAX_GENERATOR2_RANGE)/self.GENERATOR2_SCALE_FACTOR)
        return self.value

    def generator_3(self) -> float:
        return random.gauss(self.GENERATOR3_GAUSS_MEAN, self.GENERATOR3_GAUSS_SD)

    def generator_4(self,frequency) -> float:
        if frequency < self.GENERATOR3_GAUSS_MEAN and self.increment_base < self.MAX_TEMPERATURE:
            self.increment_base += self.generator_2()
        elif frequency < self.GENERATOR3_GAUSS_MEAN and self.increment_base > self.MAX_TEMPERATURE:
            self.increment_base -= self.generator_2()
        elif frequency >= self.GENERATOR3_GAUSS_MEAN and self.increment_base > self.MIN_TEMPERATURE:
            self.increment_base -= self.generator_2()
        elif frequency >= self.GENERATOR3_GAUSS_MEAN and self.increment_base < self.MIN_TEMPERATURE:
            self.increment_base += self.generator_2()

        return  self.increment_base.__round__(2)

    def singleDataGenerater(self):
        # y = [self.generator_4(self.generator_3()) for x in range(self.NUMBER_OF_VALUES)]
        # plt.plot(y, 'g')
        # plt.show()
        return self.generator_4(self.generator_3()) 

# pic=Mimic()
# pic.show()