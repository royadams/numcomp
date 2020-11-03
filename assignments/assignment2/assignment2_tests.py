import unittest
import sys
import imp
import numpy as np

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
        
## Problem 1 Tests ##       
class CourseTester(unittest.TestCase):
    fn = "assignment2.py"
    
    def test(self):
        print("*********** Testing find_roots ***********")
        Course = check_load(self.fn,"Course")
        self._test1(Course)
        self._test2(Course)
        self._test3(Course)
        
    def _test1(self,Course):
        print("---- test1 ----")
        # Create a course
        course1 = Course(590)
        
        if course1.get_course_number() != 590:
            print("result: Incorrect")
            print("course1.get_course_number() != 590")
        else:
            print("result: Correct")
            
        
    def _test2(self,Course):
        print("---- test2 ----")
        # Create a course
        course1 = Course(590)
        
        # Add a student
        course1.add_student("Joe")
        
        if course1.get_roster() != ["Joe"]:
            print("result: Incorrect")
            print("course1.get_roster() != ['Joe']")
        else:
            print("result: Correct")
            
        
    def _test3(self,Course):
        print("---- test3 ----")
        # Create a course
        course1 = Course(590)
        
        # Add two students
        course1.add_student("Joe")
        course1.add_student("Darius")
        
        # Remove a student
        course1.drop_student("Joe")
        
        if course1.get_roster() != ["Darius"]:
            print("result: Incorrect")
            print("course1.get_roster() != ['Darius']")
        else:
            print("result: Correct")
        
## Problem 2 Tests ##
class FindRootsTester(unittest.TestCase):
    fn = "assignment2.py"
    
    def run_test(self,fun,a,b,c,expected,test_name):

        print("---- %s ----"%test_name)
        print("input: %g, %g, %g"%(a,b,c))
        # Run find roots
        got = fun(a,b,c)
        print("expected: %s"%(expected,))
        print("got: %s"%(got,))
        
        # Test is the correct number of roots were returned
        if not len(got) == len(expected):
            print("result: Incorrect length")
             
        # Test if the solutions are within 1e-10
        elif np.all(np.isclose(got,expected,atol=1e-10)):
            print("result: Correct")
        else:
            print("result: Incorrect!")
            
    def test(self):
        print("*********** Testing find_roots ***********")
        fun = check_load(self.fn,"find_roots")
        self._test_simple_case_1(fun)
        self._test_simple_case_2(fun)
        self._test_a_equals_zero(fun)
        self._test_c_equals_zero(fun)
        self._test_no_solutions(fun)
        self._test_small_determinant(fun)
    
    def _test_simple_case_1(self,fun):
        a, b, c = 1.0, 7.0, 12.0
        correct_solution = [-4.0,-3.0]
        self.run_test(fun,a,b,c,correct_solution,"simple_case_1")
        
    def _test_simple_case_2(self,fun):
        a, b, c = -3.0, 5.0, 2.0
        correct_solution = [-1.0/3.0, 2.0]
        self.run_test(fun,a,b,c,correct_solution,"simple_case_2")
        
    def _test_a_equals_zero(self,fun):
        a, b, c = 0.0, 5.0, 4.0
        correct_solution = [-0.8]
        self.run_test(fun,a,b,c,correct_solution,"a_equals_zero")
    
    def _test_c_equals_zero(self,fun):
        a, b, c = 1.5, 7.2 ,0.0
        correct_solution = [-4.8, 0.0]
        self.run_test(fun,a,b,c,correct_solution,"c_equals_zero")
        
    def _test_no_solutions(self,fun):
        a, b, c = 4.0, 5.0, 4.0
        correct_solution = []
        self.run_test(fun,a,b,c,correct_solution,"no_solutions")
        
    def _test_small_determinant(self,fun):
        a, b, c = 1e-8, 10.0, 1e-8
        correct_solution = [-1e9, -1e-9]
        self.run_test(fun,a,b,c,correct_solution,"small_determinant")
    
if __name__=="__main__":
    if len(sys.argv) > 1:
        fn = sys.argv.pop()
        FindRootsTester.fn = fn
        CourseTester.fn = fn
        
    unittest.main()