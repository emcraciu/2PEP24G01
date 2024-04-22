class Car:
    __drive = '4x4'

    def check_valid_drive(self, value):
        if value not in ['4x4', '2x0']:
            raise Exception('Not a valid drive')

    @property
    def drive(self):
        return str(self.__drive + '_changed')

    @drive.setter
    def drive(self, value):
        self.check_valid_drive(value)
        self.__drive = value

    @drive.deleter
    def drive(self):
        del self.__drive


car = Car()
print(car.drive)
try:
    car.drive = '2x0'
except:
    print(f'Value not changed: {car.drive}')
else:
    print(f'Value changed: {car.drive}')

print(car._Car__drive)
del car.drive
print(car._Car__drive)
