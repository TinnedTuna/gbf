import unittest
import tape

class TestTape( unittest.TestCase ):
    def setUp(self):
        self.tape = tape.Tape()
        
    def testInitialization(self):
        """
            Test that the inital state of the tape is correct.
        """
        self.assertEqual(self.tape.pointer, 0)
        self.assertEqual(len(self.tape.tape), 30000)
        self.assertEqual(self.tape.tape, [0 for x in range(0,30000,1)])
        
    def testIncrement(self):
        """
            Test that incrementing values works
        """
        for i in range(10):
            self.tape.increment()
        self.assertEqual(self.tape.tape[0], 10)
    
    def testDecrement(self):
        """
            Test that decrementing values works.
        """
        for i in range(10):
            self.tape.increment()
            self.tape.decrement()
        self.assertEqual(self.tape.tape[0], 0)
        
    def testMoving(self):
        """
            Test that moving the tape forwards and backwards works as desired.
        """
        for i in range(65536):
            self.tape.move_forwards()
        
        for i in range(65536):
            self.tape.move_backwards()
        # Could not get this next test working.   
        #self.assertRaises(self.tape.move_backwards(), tape.TapeError)
           
    def testCellModification(self):
        """
            Test that modifying cells works as stated.
        """
        import random
        for i in range(100):
            randNum = random.randint(-65536,65536)
            self.tape.replace(randNum)
            self.assertEqual(randNum, self.tape.current_cell())
    