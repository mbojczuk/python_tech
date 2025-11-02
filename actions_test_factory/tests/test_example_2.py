from .base_test import BaseTest
from typing import Dict

class ExampleTest2(BaseTest):

    name = "example_test_2"

    def __init__(self):
        # this will use class level name and pass to BaseTest
        super().__init__(self.name)

    def run(self) -> Dict[str, str]:
        return {"status": "success", "message": f"Running example test 2: {self.name}"}