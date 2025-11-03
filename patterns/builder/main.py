from director import Director
from mycomputer_builder import MyComputerBuilder
from budget_builder import BudgetBuilder

computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

computer_builder = Director(BudgetBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()