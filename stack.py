"""
    A nice little wrapper for a stack class
"""

class Stack():
    def __init__(self):
        """
            Initialize an empty stack
        """
        self.stack=[]
    
    def pop(self):
        """
            Get an element of the top of the stack
        """
        try:
            return self.stack.pop()
        except:
            raise Exception("Stack underflow.")
        
    def push(self, val=None):
        """
            Push an element onto the top of the stack
        """
        if (val == None):
            raise ValueError("Must put a none-None value on the stack")
        else:
            self.stack.append(val)
            return True
            
    def __len__(self):
        """
            Find the size of this stack
        """
        return len(self.stack)

    def __str__(self):
        """
            Show a str representation of this object
        """
        return str(self.stack[:5]) # First 5 elements