class Computer:
    def __init__(self):
        self.case = None
        self.mainboard = None
        self.cpu = None
        self.memory = None
        self.hard_drive = None
        self.video_card = None

    def display(self):
        print("Computer Configuration:")
        print(f"  Case: {self.case}")
        print(f"  Mainboard: {self.mainboard}")
        print(f"  CPU: {self.cpu}")
        print(f"  Memory: {self.memory}")
        print(f"  Hard Drive: {self.hard_drive}")
        print(f"  Video Card: {self.video_card}")