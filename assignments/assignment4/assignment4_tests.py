import numpy as np
import numpy.linalg as la
import timeit
import unittest
from sklearn.linear_model import LinearRegression
import sys
from assignment4 import generate_data
import imp

def check_load(filename,fun_name):
    try:
        user_module = imp.load_source("module",filename)
        if hasattr(user_module,fun_name) and callable(user_module.__dict__[fun_name]):
            print("%s was succesfully loaded"%fun_name)
            return user_module.__dict__[fun_name]
        else:
            print("%s is not defined"%fun_name)
            return None
    except:
        print("Unable to load %s from %s"%(fun_name,filename))
        return None

class TestGaussJordan(unittest.TestCase):
    fn = "assignment4.py"
    
    def test(self):
        print("*********** Testing gauss_jordan ***********")
        gauss_jordan = check_load(self.fn,"gauss_jordan")
        self._test1(gauss_jordan,"test 1")
        self._test2(gauss_jordan,"test 2")
        self._test_non_invertable(gauss_jordan,"test non-invertible")
    
    def _test1(self,gauss_jordan,test_name):
        """
            The first example from the slides.
        """
        print("---- %s ----"%test_name)
        A = np.array([[1,3],[2,5]])
        A_inv = np.array([[-5,3],[2,-1]])
        got = gauss_jordan(A)
        print("input:")
        print(A)
        print("expected:")
        print(A_inv)
        print("got:")
        print(got)

        if np.all(np.isclose(got,A_inv)):
            print("result: Correct")
        else:
            print("result: Incorrect!")
        
    
    def _test2(self,gauss_jordan,test_name):
        """
            The second example from the slides.
        """
        print("---- %s ----"%test_name)
        A = np.array([[2,3,0],[1,-2,-1],[2,0,-1]])
        A_inv = np.array([[2,3,-3],[-1,-2,2],[4,6,-7]])
        got = gauss_jordan(A)
        print("input:")
        print(A)
        print("expected:")
        print(A_inv)
        print("got:")
        print(got)

        if np.all(np.isclose(got,A_inv)):
            print("result: Correct")
        else:
            print("result: Incorrect!")
        
    def _test_non_invertable(self,gauss_jordan,test_name):
        """
            A non-invertible example.
        """
        print("---- %s ----"%test_name)
        A = np.array([[2,3,0],[1,-2,-1],[2,-4,-2]])
        got = gauss_jordan(A)
        print("input:")
        print(A)
        print("expected:")
        print(None)
        print("got:")
        print(got)

        if got is None:
            print("result: Correct")
        else:
            print("result: Incorrect!")
        
class TestLinearRegression(unittest.TestCase):
    fn = "assignment4.py"

    def test(self):
        print("*********** Testing linear regression ***********")
        self._test_linear_regression_inverse()
        self._test_linear_regression_moore_penrose()

    def _test_linear_regression_inverse(self):
        # load function
        print("---- test linear_regression_inverse ----")
        linear_regression_inverse = check_load(self.fn,"linear_regression_inverse")
        
        # generate data
        n = 10
        m = 5
        X,y = generate_data(n,m)
    
        # Get correct answer from reference implementation
        lr = LinearRegression(fit_intercept = False)
        lr.fit(X,y)
        beta = lr.coef_
    
        # Run linear_regression_inverse
        got = linear_regression_inverse(X,y)
    
        if np.all(np.isclose(got,beta)):
            print("result: Correct")
        else:
            print("result: Incorrect")

    def _test_linear_regression_moore_penrose(self):
        # load function
        print("---- test linear_regression_moore_penrose ----")
        linear_regression_moore_penrose = check_load(self.fn,"linear_regression_moore_penrose")
        
        # generate data
        n = 10
        m = 5
        X,y = generate_data(n,m)
    
        # Get correct answer from reference implementation
        lr = LinearRegression(fit_intercept = False)
        lr.fit(X,y)
        beta = lr.coef_
    
        # Run linear_regression_moore_penrose
        got = linear_regression_moore_penrose(X,y)
    
        if np.all(np.isclose(got,beta)):
            print("result: Correct")
        else:
            print("result: Incorrect")
            
if __name__=="__main__":
    if len(sys.argv) > 1:
        fn = sys.argv.pop()
        TestGaussJordan.fn = fn
        TestLinearRegression.fn = fn
        
    unittest.main()