import unittest

loader = unittest.TestLoader()
suite = loader.discover('tests')
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)