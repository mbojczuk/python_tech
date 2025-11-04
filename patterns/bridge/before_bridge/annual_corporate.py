from annual import Annual

class AnnualCorporate(Annual):
    @property
    def price(self):
        return super().price * .8