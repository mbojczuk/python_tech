from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

class AbsSubscription(ABC):

    def __init__(self, subscriber: str, enrolled: datetime, discount: Any):
        self._subscriber = subscriber
        self._enrolled = enrolled
        self._discount = discount()

    @property
    def subscriber(self):
        return self._subscriber
    
    @property
    def enrolled(self):
        return self._enrolled
    
    @property
    @abstractmethod
    def price_base(self):
        pass

    @property
    def price(self):
        discount = self._discount.discount
        return self.price_base * (1-discount/100)

    @property
    @abstractmethod
    def expiration(self):
        pass