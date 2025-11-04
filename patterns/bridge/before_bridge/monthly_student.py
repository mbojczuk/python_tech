from monthly import Monthly

class MonthlyStudent(Monthly):

    @property
    def price(self):
        return super().price * .9