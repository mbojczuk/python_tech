from vend_adapter import VendAdapter
from vendor import Vendor

MOCKVENDORS = (
    VendAdapter(Vendor('Dough Factory', 1, 'Semolina Court')),
    VendAdapter(Vendor('Farmhouse', 123, 'Semo Drive')),
    VendAdapter(Vendor('Driver Ton', 33, 'Driver Avenue'))
)