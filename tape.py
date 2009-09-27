"""
    A Tape

    Represents a tape, initialized to 0s with a few functions predefined on it.
"""

class TapeError( Exception ):
    pass

class Tape(object):
    """
        A Tape Object

        This tape object will automatically expand to the right should an
        overflow be detected. Default size is 30,000.
    """
    def __init__(self):
        """
           Initalize the tape
          
           This tape initially has 30,000 cells and all are 0
        """
        self.tape = [0 for x in range(1,30001,1)]
        self.pointer = 0

    def increment(self):
        """
            Increment the value under the pointer
        """
        try:
            self.tape[self.pointer]+=1
        except:
            self.expand()
            self.tape[self.pointer]+=1

    def decrement(self):
        """
            Decrement the value under the pointer
        """
        try:
            self.tape[self.pointer]-=1
        except:
            self.expand()
            self.tape[self.pointer]-=1

    def move_forwards(self):
        """
            Move the tape forwards

            This actually just increments the internal pointer. Also deals with if the tape is
            all used, declares more tape. Doubles the length of the tape when more is needed.
        """
        if ((self.pointer) == len(self.tape)):
             self.expand()
        self.pointer+=1

    def move_backwards(self):
        """
            Move the tape backwards.

            As in the move_forwards, just decrements an internal pointer.
        """
        if (self.pointer == 0):
            raise TapeError
        self.pointer-=1

    def replace(self, value=None):
        """
            Replace the value of the current cell

            The current cell will be replaced the value given. This raises an 
            error on value not being specified
        """
        if (value == None):
            raise TapeError
        else:
            self.tape[self.pointer] = value # No value wrapping to make large
                                            # value calculations easier.

    def current_cell(self):
        """
            Get the value of the current cell
        """
        return self.tape[self.pointer]
    
    def __getitem__(self, i=None):
        """
            Get the i-th element of this tape
        """
        if  (i!=None):
            return self.tape[i]

    def __eq__(self, other_tape):
        """
            Test that this tape is equal to another.
        """
        return (self.tape == other_tape.tape)
    
    def __ne__(self, other_tape):
        """
            Test if this tape is not equal to another.
        """
        return (self.tape != other_tape.tape)

    def __len__(self):
        """
            Return the length of this tape.
        """
        return len(self.tape)
    def expand(self):
        """
            Double the length of this tape with fresh 0s
        """
        self.tape += [0 for x in range(len(self.tape))]