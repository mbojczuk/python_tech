""" 
Builder pattern example:
 - Creational pattern
 - Sperate construction of an object from its representation
 - Obey the prinicipal and encapsulates object consstruction
 - multistep construction process
 - implementations may vary
 - client only sees the abstraction
"""
from abc import ABC, abstractmethod
from computer import Computer

# base class has examples that would be repeated in each example
# for more abstract classes then they should probably be abstract also for computer and have the child class implement it also
class Builder(ABC):
    
    def get_computer(self) -> Computer:
        return self._computer
    
    def new_computer(self):
        self._computer = Computer()
    
    @abstractmethod
    def build_mainboard(self):
        pass

    @abstractmethod
    def get_case(self):
        pass

    @abstractmethod
    def install_mainboard(self):
        pass

    @abstractmethod
    def install_hard_drive(self):
        pass

    @abstractmethod
    def install_video_card(self):
        pass