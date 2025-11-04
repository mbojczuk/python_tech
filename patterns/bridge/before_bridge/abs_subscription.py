from abc import ABC, abstractmethod
from datetime import datetime

class AbsSubscription(ABC):

    def __init__(self, subscriber: str, enrolled: datetime):
        self._subscriber = subscriber
        self._enrolled = enrolled

    @property
    def subscriber(self):
        return self._subscriber
    
    @property
    def enrolled(self):
        return self._enrolled
    
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def expiration(self):
        pass