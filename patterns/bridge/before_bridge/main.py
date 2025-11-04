from annual_corporate import AnnualCorporate
from annual_student import AnnualStudent

from monthly_corporate import MonthlyCorporate
from monthly_student import MonthlyStudent

from monthly import Monthly
from annual import Annual

from datetime import datetime

def main():
    # Discounted
    sub1 = MonthlyStudent('bob', datetime.today())
    sub2 = MonthlyCorporate('Jess', datetime.today())

    sub4 = AnnualStudent('Steven', datetime.today())
    sub3 = AnnualCorporate('Denice', datetime.today())
    

    print(f'Sub: {sub1.subscriber}, Code: {sub1.price}, Expiration: {sub1.expiration}')
    print(f'Sub: {sub2.subscriber}, Code: {sub2.price}, Expiration: {sub2.expiration}')

    print(f'Sub: {sub4.subscriber}, Code: {sub4.price}, Expiration: {sub4.expiration}')
    print(f'Sub: {sub3.subscriber}, Code: {sub3.price}, Expiration: {sub3.expiration}')

    # normal
    sub5 = Annual('Dave', datetime.today())
    sub6 = Monthly('Emma', datetime.today())

    print(f'Sub: {sub5.subscriber}, Code: {sub5.price}, Expiration: {sub5.expiration}')
    print(f'Sub: {sub6.subscriber}, Code: {sub6.price}, Expiration: {sub6.expiration}')

if __name__ == "__main__":
    main()