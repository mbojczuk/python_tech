from annual import Annual

class AnnualStudent(Annual):
    @property
    def price(self):
        return super().price * .9