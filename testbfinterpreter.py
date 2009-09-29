import unittest
import bfinterpreter
import tape

class TestBFInterpreter( unittest.TestCase ):
    def setUp(self):
        self.bfi = bfinterpreter.BFInterpreter()
    
    def testPreprocessor(self):
        """
            Test that the preprocessor works.
            
            The example code has 3 lines and plenty of comments
        """
        code = """+++++ Put 5 in the first cell
                  [>+>+<<-] copy it destructively into the next two
                  >>[<<+>>-] copy the last one destructively into the first cell"""
        self.bfi.preprocess_program(code)
        self.assertEqual(self.bfi.program, list("+++++[>+>+<<-]>>[<<+>>-]"))
        
    def testEmptyProgram(self):
        """
            Test that nothing wierd happens on executing an empty program.
        """
        self.bfi.preprocess_program("")
        self.bfi.execute()
        self.assertEqual(tape.Tape(), self.bfi.tape)
         
               
    def testBasicExecution(self):
        """
            Test the most basic execution. Put 5 in two cells
        """
        code =">+++++[>+>+<<-]" # Has almost all the most basic elements, bar I/O
        self.bfi.preprocess_program(code)
        self.bfi.execute()
        self.assertEqual(5, self.bfi.tape[2]) # Check that the right answer is left on the tape
        
    def testTwoLoops(self):
        """
            Test a program with two loops in it.
        """
        code = "+++++[>+>+<<-]>>[<<+>>-]" # Duplicates the number 5 into the second cell non destrictively.
        self.bfi.preprocess_program(code)
        self.bfi.execute()
        self.assertEqual([5,5], [self.bfi.tape[0],self.bfi.tape[1]])
        
    def testBasicNesting(self):
        """
            Test a program with a nested loop, one level deep.
        """
        code = ">+>+[[-]<]" # Set up a line and run back and clear them.
        self.bfi.preprocess_program(code)
        self.bfi.execute()
        self.assertEqual([0,0], self.bfi.tape[0:2]) # The tape should be reset after this code.
        
    def testNestedLoops(self):
        """
            Test a program with nested loops.
            
            The example program should calculate the factorial of 3, 6
        """
        fact=">+++[>[-]>[-]<<[->+>+<<]>>[-<<+>>]<-]<<[[>[>+>+<<-]>>[<<+>>-]<<<-]>>[<<+>>-]<[-]<<]>[<+>-]<"
        self.bfi.preprocess_program(fact)
        self.bfi.execute()
        self.assert_(6 in self.bfi.tape[0:5])
        
    def testJumpMap(self):
        """
            Test that the jump map gets built correctly.
        """
        code = "[+++++>]<-COMMENT-+=[morecomment[++--]>>]++--<><><[ More nesting [-[+]]<[-]]"
        self.bfi.preprocess_program(code)
        self.bfi.build_jump_map(self.bfi.program)
   #     print "\n\n"+str(self.bfi.jump_map)+"\n\n"
        #self.assertEqual()
        #self.assert_(len([key for key in self.bfi.jump_map if key<self.bfi.jump_map[key]]) == len(self.bfi.jump_map))
        self.assertEqual(len(self.bfi.jump_map), len(filter((lambda (n) : n == "]"), self.bfi.program))*2)

    def testBasicCellClear(self):
       """
           Test that the cell clear ("[-]") loop works as intended
       """
       code = "++++++++[-]"
       self.bfi.preprocess_program(code)
       self.bfi.execute()
       self.assertEqual(self.bfi.tape[0],0)   
    

    def testMore(self):
        """
            Test a fairly long-ish program
        """
        code =">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.>>>++++++++[<++++>-]<.>>>++++++++++[<+++++++++>-]<---.<<<<.+++.------.--------.>>+.>>[[-]<][-]<<<[-]"
        self.bfi.preprocess_program(code)
        self.bfi.execute()
        self.assert_(0== self.bfi.tape[0])

    def testRewindClear(self):
        """
            Test that one can rewind along the tape, clearing it.
        """
        self.bfi.preprocess_program(">+>++->+++>+>+>++++++>+++++>+[[-]<]")
        self.bfi.execute()
        self.assertEqual([0,0,0,0,0,0,0,0], self.bfi.tape[0:8])
        
#===============================================================================
#    def testIO(self):
#       """
#           Test the IO of the interpretter.
#           
#           Requires interaction!
#       """
#       code = ",.[-]"
#       self.bfi.preprocess_program(code)
# #      self.bfi.execute()
#       self.assertEqual(tape.Tape(), self.bfi.tape)
#       
#===============================================================================
if (__name__=="__main__"):
#    suite = unittest.TestLoader().loadTestsFromTestCase(TestBFInterpreter)
 #   unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
