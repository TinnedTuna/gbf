import math
import random
import sandbox

class OrganismError():
    pass

class Organism(object):
    """
        A class to represent a single organism.
    """
    def __init__(self, code=None, base_fitness=None):
        """
            Initialize this organism with some code.
        """
        print code, base_fitness
        if (code==None):
            raise OrganismError("No initial value supplied")
        else:
            self.dies=False
            self.code=code
            self.tape_top = None
            self.sbox = sandbox.Sandbox(3,2000) # 3 seconds to run, max
            self.mutation_prob=0.45
            self.mutation_list = [True]+[False for x in range(int(1/self.mutation_prob)-1)]
            random.shuffle(self.mutation_list)
        if (base_fitness is None):
            self.fitness = None
        else:
            self.fitness = base_fitness
            
    def evaluate(self, target=None):
        """
            Evaluate this organism by running it
        """
        if (target==None):
            raise OrganismError("No target!")
        try:
            result = self.sbox.run(self.code) # Run the code
        except:
            self.dies=True
            result = False
        if (result):
            self.tape_top = self.sbox.top_of_tape(10)
            # This is where the fitness is decided.
            # The distance is always atleast one, so that it can be affected
            # by the length of the input code.
            # We can then try to evolve the shortest algorithm :-)
            self.fitness = (self.distance(self.tape_top, target)+1)+(math.exp(0.001*len(self.code)))
        else:
            # This organism dies
            self.fitness=None
            self.dies = True
        if (len(self.code) == 0):
            self.fitness =None
            self.dies = True
            
        
        
    def __cmp__(self, other_org=None):
        """
            Compare this organism with another.
        """
        if (self.dies or self.fitness==None):
             return -1 # It has died, it must be worse than anything.
        else:
            if (self.fitness > other_org.fitness):
                 return -1
            elif (self.fitness < other_org.fitness):
                 return 1
            else:
                 return 0
            
        
    def distance(self, first_tape, second_tape):
        """
            Calculate the distance between this and another tape.
        """
        pairs = zip(first_tape, second_tape)
        return math.sqrt(abs(sum(map((lambda n: self.subsq(*n)), pairs))))
        
    def subsq(self, a, b):
        """
            The distance between 2 values
        """
        return ((a-b)**2)
    
    def breed(self, mate=None):
        """
            Breed this organism with a selected mate
        """
        our_code = self.code
        mate_code = mate.code
        instructs = ["+","-","[","]","<",">"]
        randint = random.randint(0, len(our_code))
        # Splice them together at random
        result_gene=(our_code[0:randint-1]+mate_code[randint:])
        # Optionally add/remove some info.
        if (random.choice(self.mutation_list)):
            if (random.choice([True, False, False, False,])):
                # Add info
                result_gene = result_gene+ random.choice(instructs)
            else:
                # Remove info
                result_gene = result_gene[:-1]
        try:
            if (random.choice(self.mutation_list)):
                rand = random.randint(0,len(result_gene))
                result_gene = result_gene[:rand-1] + random.choice(instructs) + result_gene[rand:]
        except:
            print "Error mutating genome"
                
        # Make a baby organism! *squee*
        return Organism(result_gene)
                
        
    def __str__(self):
        """
            A string representation of this organism
        """
        return str((self.code, self.fitness,))
