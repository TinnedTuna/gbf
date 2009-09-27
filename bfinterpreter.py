import sys

import stack
import tape
"""
    Brainfuck interpreter

    Uses a bre-built map of where to jump as an optimization. Code must be 
    preprocessed, this is not a repl.
"""


class BFInterpreter():
    def __init__(self):
        self.tape = tape.Tape()
        #self.stack = stack.Stack() # Stack for loops
        self.instruction_pointer = 0 # Current instruction
        self.program = [] # The program
        self.instructions = { ">":self.tape.move_forwards, \
                              "<":self.tape.move_backwards, \
                              "+":self.tape.increment, \
                              "-":self.tape.decrement, \
                              "[":self.enter_loop, \
                              "]":self.end_loop, \
                              ".":self.output, \
                              ",":self.input, \
                              "#":self.debug \
                            }
        self.jump_map = {} # A place to look for corresponding braces
        
    def preprocess_program(self, input_code=None):
        """
            Preprocess the brainfuck
            
            Remove comments, split each individual instruction into the 
            program tape. Clear the memory tape for the next execution.
        """
        if (input_code == None):
            return;
        map(self.program.append, filter((lambda (char): char in self.instructions), input_code))
        #self.program.append(False) # Causes interpretation to stop after the program has finished.
        self.build_jump_map(self.program)
    
    def build_jump_map(self, input_program):
        """
            Build a map of where each "]" has an opening "[".
            
            input_program must be a list of bf commands.
        """
        open_bracket_stack = stack.Stack()
        for inst, command in enumerate(input_program):
            if command in (">","<","+","-",".",",","#",):
                # Ignore all normal brainfuck characters.
                pass
            elif (command=="["):
                # We've found one, push it's location onto the stack.
                open_bracket_stack.push(inst)
            elif (command=="]"):
                # We've found a closing one. Map this location to the location
                # on the top of the stack 
                try:
                    previous_bracket = open_bracket_stack.pop()
                    self.jump_map[previous_bracket]=inst
                    self.jump_map[inst] = previous_bracket
                except:
                    print "Missing open bracket."
        #print self.jump_map        
        
    def output(self):
        """
            Outputs the value of the current cell.
        """
        try:
            sys.stdout.write(chr(self.tape.current_cell()%256)) # Wrapping fits it into ascii codes
        except:
            print "Error -001"
            
    def input(self):
        """
            Set the current cell to a new value
        """
        try:
            temp = ord(raw_input())
            self.tape.replace(temp)
        except:
            print "Error -002"
    
    def enter_loop(self):
        """
            Do the code goodness for entering a loop.
        """
        if (self.tape.current_cell()==0):
            # Jump past the end.
            self.instruction_pointer = (self.jump_map[self.instruction_pointer])
        else:
            pass

        
    def end_loop(self):
        """
            Jump to the start of the loop if the current cell is not 0.
        """
       # if (not self.tape.current_cell()):
            # Jump to the start of the loop
        self.instruction_pointer = (self.jump_map[self.instruction_pointer]-1)
        #else:
        #    pass
   
        
    def execute(self):
        """
            Execute the cleaned brainfuck program
            
            Will only correctly run after preprocess_program() has been run.
        """
        while len(self.program)>(self.instruction_pointer):
            self.step()
       #self.tape = tape.Tape() # Clear for next time.
       
    def step(self):
       """
           Do a single step in a brainfuck program
       """
       try:
           self.instructions[self.program[self.instruction_pointer]]()
           self.instruction_pointer+=1
       except tape.TapeError:
           print "Tape underflow, instruction number: "+str(self.instruction_pointer)
           raise

    def debug(self):
        """
            Print debugging information.
        """
        print "Tape: "+str(self.tape.tape[:10])+" Current Pointer: "+str(self.tape.pointer)+" Instruction Pointer: "+str(self.instruction_pointer)
        
    def clear_tape(self):
        """
            Clear the tape for next round.
        """
        self.tape = tape.Tape()
        
    def __str__(self):
        """
            A string representation of the interpreter
        """
        return str((self.instruction_pointer, self.program,))
    
    def __len__(self):
        """
            The length of this brainfuck interpreter
        """
        return len(self.tape)