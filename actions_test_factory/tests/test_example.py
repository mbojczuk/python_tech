from .base_test import BaseTest
from typing import Dict

class ExampleTest(BaseTest):

    name = "example_test"

    def __init__(self):
        # this will use class level name and pass to BaseTest
        super().__init__(self.name)

    def run(self) -> Dict[str, str]:
        return {"status": "success", "message": f"Running example test: {self.name}"}