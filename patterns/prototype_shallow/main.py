from laptop import Laptop
from tower import Tower, MainBoard

# l1 = Laptop('L1', 'Intel', '32GB', '2TB SSD', 'onboard', '1980x1080')
# l1.display()
# l2 = l1.clone()
# l2.model = 'L2'
# l2.processor = 'AMD'
# l2.display()

t1 = Tower('T1', MainBoard('ASUS', 'Game'), 'AMD', '32GB', '2TB SSD', 'onboard', '1980x1080')
t1.display()
t2 = t1.clone() # this preforms a shallow copy so it keeps reference to object so if you do a shallow clone it will change both
t2.model = 'T2'
t2.mainBoard.model = 'Business'
t1.display()