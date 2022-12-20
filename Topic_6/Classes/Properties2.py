class Car:
    __speed = 0
    __asKPH = True

    @property
    def speed(self):
        if self.__asKPH:
            kph = self.__speed * 8 / 5
            return kph
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if 0 <= speed <= 70:
            self.__speed = speed

    def accelerate(self, amount):
        self.speed += amount
