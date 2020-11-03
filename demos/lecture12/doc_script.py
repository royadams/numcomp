"""
    doc_script
    Place a docstring at the top of a script to document usage.

    Usage:
        python -h script.py """

def fun(args):
    """
        Place a docstring under a def statement to document a function.
        Call help(fun) to view the docstring.

        Inputs: Describe the inputs.

        Outputs: Describe the outputs.

        Raises: Describe the possible exceptions."""
    pass
    
class Foo:
    """
        Place a docstring under a class statement to document a class.
        Call help(Foo) to view the docstring."""
    
    var = 2
    
    def __init__(self):
        """ __init__ docstring """
    
    def member_function(self):
        """
            member_function docstring """
        pass