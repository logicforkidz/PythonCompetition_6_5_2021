import unittest
import inspect
from ideal import evaluate_string
#evaluate_string = evaluate_strings

class MyTestCase(unittest.TestCase):

    currentResult = None # holds last result object passed to run method

    @classmethod
    def setResult(cls, amount, errors, failures, skipped):
        cls.amount, cls.errors, cls.failures, cls.skipped = \
            amount, errors, failures, skipped

    @classmethod
    def tearDownClass(cls):
        failed = len(cls.errors) + len(cls.failures)
        success = cls.amount - failed
        percent = round((success - failed)*10/cls.amount, 1)
        print(f"\nTests run:{cls.amount} Passed:{success} Failed:{failed}")
        print(f"Score: {percent}")
        #print("errors: " + str(len(cls.errors)))
        #rint("failures: " + str(len(cls.failures)))
        #print("success: " + str(cls.amount - len(cls.errors) - len(cls.failures)))
        #print("skipped: " + str(len(cls.skipped)))

    def tearDown(self):
        amount = self.currentResult.testsRun
        errors = self.currentResult.errors
        failures = self.currentResult.failures
        skipped = self.currentResult.skipped
        self.setResult(amount, errors, failures, skipped)

    def run(self, result=None):
        self.currentResult = result # remember result for use in tearDown
        unittest.TestCase.run(self, result) # call superclass run method

    def test_a(self):
        name = inspect.currentframe().f_code.co_name
        s = " 7 - 2 + 3"
        ret = 8
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_b(self):
        name = inspect.currentframe().f_code.co_name
        s = "3 -1 + 3"
        ret = 5
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_c(self):
        name = inspect.currentframe().f_code.co_name
        s = " 4 +3+2+2+1+9    -1"
        ret = 20
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_d(self):
        name = inspect.currentframe().f_code.co_name
        s = " 5 -5 +5 -5-5-5 +5+5 +5 -2-3+2+3-5"
        ret = 0
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_e(self):
        name = inspect.currentframe().f_code.co_name
        s = "+5 -5"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_f(self):
        name = inspect.currentframe().f_code.co_name
        s = "-5 -5"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_g(self):
        name = inspect.currentframe().f_code.co_name
        s = "5 -5-"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_h(self):
        name = inspect.currentframe().f_code.co_name
        s = "5 -5 +"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_i(self):
        name = inspect.currentframe().f_code.co_name
        s = "5*5"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_j(self):
        name = inspect.currentframe().f_code.co_name
        s = "5+a"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_k(self):
        name = inspect.currentframe().f_code.co_name
        s = "11-1"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_l(self):
        name = inspect.currentframe().f_code.co_name
        s = "5-+5"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")

    def test_m(self):
        name = inspect.currentframe().f_code.co_name
        s = "2 2"
        ret = None
        got = evaluate_string(s)
        print (f"{name}: Trying input:\"{s}\"")
        self.assertEqual(ret,got, f"Failed {name}. Input:\"{s}\" Expected Output:{ret} but got:{got}")


if __name__ == '__main__':
    unittest.main()
