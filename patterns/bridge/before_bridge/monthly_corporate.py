from monthly import Monthly

class MonthlyCorporate(Monthly):
    @property
    def price(self):
        return super().price * .8