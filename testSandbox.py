import unittest
import sandbox

class TestSandbox( unittest.TestCase ):
    """
        Test that the sand box works, hopefully.
    """
    
    def setUp(self):
        pass
    
    def testTime(self):
        """
            Test that this returns false for an object that would clearly
            exceed any time limit.
        """
        box = sandbox.Sandbox(5, 300000) # 100 seconds, 300000 of mem max
        code = "++[++]"
        self.assertEqual(False, box.run(code))
        
    def testMemory(self):
        """
            Test that this returns false for an object that would exceed any memory limit
        """
        box = sandbox.Sandbox(100000, 30005) # 100000 seconds, 30005 mem max
        code = "+[>+]"
        self.assertEqual(False, box.run(code))
        
    def testNeither(self):
        """
            A program that will not exceed the limits, hopefully
        """
        box = sandbox.Sandbox(30,30001) # 30 secs, 30001 max mem
        code = ">+++[>[-]>[-]<<[->+>+<<]>>[-<<+>>]<-]<<[[>[>+>+<<-]>>[<<+>>-]<<<-]>>[<<+>>-]<[-]<<]>[<+>-]<"
        self.assertEqual(True, box.run(code))