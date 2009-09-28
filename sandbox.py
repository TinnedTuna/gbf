import bfinterpreter
import time

class SandboxError(object):
    pass

class Sandbox(object):
    """
        This is a sandbox for running limited brainfuck programs
    """
    def __init__(self, max_time=None, max_mem=None):
        """
            Setup the sandbox.
            
            This can accept a maximum time for running, a maximum memory 
            allocation allowed.
        """
        if (max_time==None):
            self.max_time=10000
        else:
            self.max_time = max_time
        if (max_mem==None):
            self.max_mem=10000
        else:  
            self.max_mem = max_mem    
        self.start_time = None
            
    def run(self, code=None):
        """
            Run some code in this sandbox
        """
        if (code==None):
            return False
        self.bfi = bfinterpreter.BFInterpreter(1000)
        self.bfi. preprocess_program(code)
        self.start_time = int(time.time())
        while len(self.bfi.program)>(self.bfi.instruction_pointer):
            if (not self.exceeded()):
                self.bfi.step()
            else:
                return False
        return True
            
    def exceeded(self):
        """
            Return true if this code has exceeded it's memory or time allowance
        """
        return (self.max_mem < len(self.bfi.tape)) or (self.max_time <  (int(time.time()) - self.start_time))
    
    def top_of_tape(self, n=None):
        """
            Get the first n elements of the tape.
        """
        if (n==None):
            raise SandboxError("No value given")
        else:
            return self.bfi.tape[0:n]
