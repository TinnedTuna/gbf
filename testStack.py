import unittest
import stack

class TestStack( unittest.TestCase ):
    def setUp(self):
        """
            Just create an empty stack
        """
        self.stack = stack.Stack()
        
    def testEmptySize(self):
        """
           Check that an empty stack always has size 0 
        """
        self.assertEqual(0,len(self.stack)) # Should be 0
        self.stack.push("val")
        self.stack.pop()
        self.assertEqual(0,len(self.stack)) # Should still be 0
        try:
            self.stack.pop()
        except:
            pass
        self.assertEqual(0,len(self.stack)) # It's 0 even after an error
    
    def testSize(self):
        """
            Test that the size remains sane
        """
        self.assert_(0 == len(self.stack))
        for i in range(1,10,1):
            self.stack.push(i)
            self.assertEqual(len(self.stack),i)
        
if (__name__=="__main__"):
    unittest.main()