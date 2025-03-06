import unittest
import os
import sys

# Ensure the script runs from the tests directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

test_loader = unittest.TestLoader()
test_suite = test_loader.discover(".")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)
