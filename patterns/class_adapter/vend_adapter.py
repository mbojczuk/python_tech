from customer import Customer
from vendor import Vendor

# interface inherits from adapter class
class VendAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @property
    def address(self):
        return f'{self.number} {self.street}'