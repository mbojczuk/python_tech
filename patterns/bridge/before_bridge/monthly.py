from abs_subscription import AbsSubscription
from dateutil.relativedelta import relativedelta

class Monthly(AbsSubscription):

    @property
    def price(self):
        return 50.00
    
    @property
    def expiration(self):
        return self._enrolled + relativedelta(months=1)