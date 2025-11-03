from builder import Builder

class MyComputerBuilder(Builder):

    def get_case(self):
        self._computer.case = 'Coolermaster'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI'
        self._computer.cpu = 'Intel Core i9'
        self._computer.memory = '2 X 16GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'SSD'

    def install_video_card(self):
        self._computer.video_card = 'GeForce GTX'