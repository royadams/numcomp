import numpy as np
import numpy.linalg as la
import unittest
import sys
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

###########################################
# Testing Code
###########################################

class InverseCDFTester(unittest.TestCase):
    fn = "assignment5.py"

    def test(self):
        print("*********** Testing linear regression ***********")
        self.inverse_normal_cdf = check_load(self.fn,"inverse_normal_cdf")
        mu, sigma2 = 0.0,1.0
        u = np.array([0.46486431,0.13859356,0.44061447,0.34812907,0.56085382])
        expected = np.array([-0.08818627,-1.08665996,-0.14941149,-0.39037652,0.15313432])
        self._test_inverse_cdf(mu,sigma2,u,expected)
        mu, sigma2 = 1.0,2.0
        u = np.array([0.46486431,0.13859356,0.44061447,0.34812907,0.56085382])
        expected = np.array([ 0.87528576, -0.53676924,  0.78870023,  0.44792422,  1.21656462])
        self._test_inverse_cdf(mu,sigma2,u,expected)
        
    def _test_inverse_cdf(self,mu,sigma2,u,expected):
        got = self.inverse_normal_cdf(u,mu,sigma2)
        print("---- test mu=%g, sigma2=%g ----"%(mu,sigma2))
        print("u:")
        print(u)
        print("expected:")
        print(expected)
        print("got:")
        print(got)
        if np.all(np.isclose(got,expected)):
            print("result: Correct")
        else:
            print("result: Incorrect!")
    #
    # def _test_inverse_cdf1(self):
    #
    #     u = np.array([0.46486431,0.13859356,0.44061447,0.34812907,0.56085382])
    #     expected = np.array([-0.08818627,-1.08665996,-0.14941149,-0.39037652,0.15313432])
    #     got = inverse_normal_cdf(u,0.0,1.0)
    #     self.assertTrue(np.all(np.isclose(expected,got)))
    #
    #
    # def _test_inverse_cdf2(self):
    #     inverse_normal_cdf = check_load(self.fn,"inverse_normal_cdf")
    #     u = np.array([0.46486431,0.13859356,0.44061447,0.34812907,0.56085382])
    #     expected = array([ 0.87528576, -0.53676924,  0.78870023,  0.44792422,  1.21656462])
    #     got = inverse_normal_cdf(u,1.0,2.0)
    #     self.assertTrue(np.all(np.isclose(expected,got)))


if __name__=="__main__":
    if len(sys.argv) > 1:
        fn = sys.argv.pop()
        InverseCDFTester.fn = fn
        
    unittest.main()