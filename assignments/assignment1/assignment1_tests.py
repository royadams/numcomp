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
        
def _test(fun,inp,expected):
    print("---- Test 1 ----")
    print("input: %s"%(inp,))
    got = fun(inp)
    print("expected: %s"%(expected,))
    print("got: %s"%(got,))
    if expected != got:
        print("result: Incorrect!")
    else:
        types_match = type(got) == type(expected)
        if isinstance(expected,list):
            for i1,i2 in zip(expected,got):
                if type(i1) != type(i2):
                    types_match = False
                
        if types_match:
            print("result: Correct")
        else:
            print("result: Type mismatch!")

class Tester(unittest.TestCase):
    fn = "assignment1.py"
    
    def test_evens_only(self):
        print("\n")
        print("********** Testing evens_only() **********")
        fun = check_load(self.fn,"evens_only")
        if fun is not None:
            _test(fun,[1,2,3,4,5] , [2,4])
            _test(fun,[-2,-1,0,5,5,3,2,2] , [-2,0,2,2])
            _test(fun,[2.0,3.0,4.0,6.5] , [2,4])
            _test(fun,[] , [])
        
    def test_piecewise(self):
        print("\n")
        print("********** Testing piecewise() **********")
        fun = check_load(self.fn,"piecewise")
        if fun is not None:
            _test(fun,-5.0, -1.0)
            _test(fun,1.0, 3.0)
            _test(fun,5, -5.0)
        
    def test_character_count(self):
        print("\n")
        print("********** Testing character_count() **********")
        fun = check_load(self.fn,"character_count")
        if fun is not None:
            _test(fun,"test1.txt" , {'e': 1, 'g': 1, 'i': 1, 'n': 1, 's': 2, 'r': 1, 't': 3})
            _test(fun,"test2.txt" , {'a': 14, 'c': 10, 'b': 2, 'e': 25, 'd': 8, 'g': 1, 'i': 12, 'm': 10, 'l': 6, 'o': 14, 'n': 5, 'q': 1, 'p': 7, 's': 14, 'r': 8, 'u': 12, 't': 11})
            _test(fun,"test3.txt" , {})
    
if __name__=="__main__":
    if len(sys.argv) > 1:
        fn = sys.argv.pop()
        Tester.fn = fn
        
    unittest.main()