import unittest
import UnitTesting.simple


class TestSimple(unittest.TestCase):

    """
    The setup and tear down class methods run before (setup) and after (tear down) all the tests in case you
    need to do any setups before you run a test (e.g database setups etc) and then do clean up operations after
    the tests are done (e.g drop tables, remove records etc)
    """
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    """
    The setup and tear down methods are excellent for using objects in each test so rather than
    creating an object in each test, you could just create member vars to hold them and test them
    from each point without having to create objects all over the code
    """
    # runs code before each test
    def setUp(self):
        self.some_value = 100  # before test, we set to 100 for test reasons
        pass

    # runs code after each test
    def tearDown(self):
        self.some_value = 0  # after test, we set to zero for w/e reason
        pass

    """You must prefix test methods with test_ or the test module won't know it's a test"""
    def test_add(self):
        ans = UnitTesting.simple.add(5, 10)
        self.assertEqual(ans, 15)
        ans = UnitTesting.simple.add(25, 25)
        self.assertEqual(ans, 50)
        ans = UnitTesting.simple.add(5, 5)
        self.assertEqual(ans, 10)

    def test_sub(self):
        ans = UnitTesting.simple.sub(10, 5)
        self.assertEqual(ans, 5)
        ans = UnitTesting.simple.sub(100, 50)
        self.assertEqual(ans, 50)
        # raise errors, this should test that passing the args will throw an exception
        self.assertRaises(ValueError, UnitTesting.simple.divide, 10, 0)
        # use context manager to test for exception throwing
        with self.assertRaises(ValueError):
            UnitTesting.simple.divide(10, 0)


# This tells python that if this test is run, use unittest as our main
# which allows it to run our test cases above
if __name__ == '__main__':
    unittest.main()
