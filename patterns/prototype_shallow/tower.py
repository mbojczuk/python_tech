from abs_computer import AbsComputer
from abs_prototype import AbsPrototype
import copy
from dataclasses import dataclass

@dataclass
class MainBoard:
    manufacturer:str
    model: str


@dataclass
class Tower(AbsPrototype, AbsComputer):
    model: str
    mainBoard: MainBoard
    processor: str
    memory: str
    hard_drive: str
    graphics: str
    screen: str

    def display(self):
        print(f"Custom Computer: {self.model}")
        print(f'\tMainboard: {self.mainBoard.model}')
        print(f'\tProcessor: {self.processor}')
        print(f'\tMemory: {self.memory}')
        print(f'\tHard_drive: {self.hard_drive}')
        print(f'\tGraphics: {self.graphics}')
        print(f'\tScreen: {self.screen}')

    def clone(self):
        # creating a copy of the current object
        return copy.copy(self)