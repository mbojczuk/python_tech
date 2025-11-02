from test_factory import TestFactory
from typing import Dict

def run_all_tests() -> Dict[str, Dict[str, str]]:
    # Create an instance of the TestFactory
    factory = TestFactory()
    # get list of all available tests
    requested_tests = factory.available()
    # set up a results dictionary
    results: Dict[str, Dict[str, str]] = {}

    for test_name in requested_tests:
        # create test instance
        test = factory.create_instance(test_name)
        # run the test and store the result
        results[test_name] = test.run()
    return results

if __name__ == "__main__":
    all_results = run_all_tests()
    for name, result in all_results.items():
        print(f"Results for {name}: {result}")
