class Car:
    # sets two variables that should not be used by others
    __speed = 0
    __asKPH = False

    def get_speed(self):
        # if KPH is true return kph
        if self.__asKPH:
            kph = self.__speed * 8 / 5
            return kph
        # else return starting variable
        return self.__speed

    def set_speed(self, speed):
        # method to set speed if it is in range
        if 0 <= speed <= 70:
            self.__speed = speed

    # create speed object with 2 properties
    speed = property(get_speed, set_speed)

    def accelerate(self, amount):
        # method to sed acceleration amount
        self.speed += amount


