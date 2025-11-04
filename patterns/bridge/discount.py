from abc import ABC, abstractmethod

class Discount(ABC):

    # so this is a propert stacked on abstract method meaning the inherited child class needs to implement
    # while also being a value for property
    @property
    @abstractmethod
    def discount(self):
        pass

class StudentDiscount(Discount):

    @property
    def discount(self):
        return 10
    
class CorporateDiscount(Discount):

    @property
    def discount(self):
        return 20

class NoDiscount(Discount):

    @property
    def discount(self):
        return 0
