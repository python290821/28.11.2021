
from abc import ABC, abstractmethod

class Mobile(ABC):
    # data
    @abstractmethod
    def __init__(self, number):
        self.number = number
        print('creating new Mobile')

    # functions
    def ring(self):
        print(f'mobile {self.number} is ringing')

    def __str__(self):
        return f'[Mobile] number: {self.number}'

class Android(Mobile):

    def __init__(self, number, android_version):
        # option 1
        super().__init__(number)

        # option 2
        #Mobile.__init__(self, number)

        self.android_version = android_version

        # self.number = number
        print('creating new Android')

    def __str__(self):
        return f'[Android] version: {self.android_version} | ' + \
               super().__str__()

class IPhone(Android):
    pass

# mb = Mobile('053333333') # Error
a = Android('053333333', 'Kit Kat')
a.ring()
print(a)