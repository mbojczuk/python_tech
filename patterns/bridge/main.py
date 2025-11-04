from monthly import Monthly
from annual import Annual
from discount import NoDiscount, StudentDiscount, CorporateDiscount

from datetime import datetime

def main():
    # Discounted
    sub1 = Monthly('bob', datetime.today(), StudentDiscount)
    sub2 = Monthly('Jess', datetime.today(), CorporateDiscount)

    sub4 = Annual('Steven', datetime.today(), NoDiscount)
    sub3 = Annual('Denice', datetime.today(), NoDiscount)
    

    print(f'Sub: {sub1.subscriber}, Code: {sub1.price}, Expiration: {sub1.expiration}')
    print(f'Sub: {sub2.subscriber}, Code: {sub2.price}, Expiration: {sub2.expiration}')

    print(f'Sub: {sub4.subscriber}, Code: {sub4.price}, Expiration: {sub4.expiration}')
    print(f'Sub: {sub3.subscriber}, Code: {sub3.price}, Expiration: {sub3.expiration}')

if __name__ == "__main__":
    main()