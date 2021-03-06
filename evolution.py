import multiprocessing
import organism
import random

class EvolutionError():
    pass

def f(n):
    """
        Helper function, that might be picklable
    """
    n[0].evaluate(n[1])
    return (n.code,n.fitness,)
    
class Evolution():
    """
        Provides an environment for our litte bf organisms to evolve in.
    """
    def __init__(self, pop_size=None, target=None, initial=None, mp=None):
        """
            Set up the environment and a default population of pop_size
        """
        if (mp is None):
            self.multi = 0
        else:
            self.multi = mp
        if (target is None or pop_size is None):
            raise EvolutionError("Must specify BOTH pop_size and a target")
        self.population = []
        self.ppop = None
        self.instructions = (">","<","+","-","[","]")
        self.pop_size = pop_size
        self.target = target
        num = self.multi
        try:
            self.pool = multiprocessing.Pool(processes=num) # start a worker pool
        except:
            print "Could not allocate a worker pool"
        # Now seed a random population, if we've been given an initial value
        if (initial is None):
            while (len(self.population) <= self.pop_size):
                self.population.append(organism.Organism(self.random_gene()))
        else:
            # Seed the inital population
            for code in initial:
                self.population.append(organism.Organism(code))
            # Breed them!
            self.breed()


     
    def breed(self):
        """
            Breed random organisms together to get children until pop_size
        """   
        while (len(self.population) <= self.pop_size):
            orga = random.choice(self.population)
            orgb = random.choice(self.population) # Asexualism works too :-p
            self.population.append(orga.breed(orgb)) # Add a new organism
            
    def random_gene(self):
        """
            Generate a random genome
        """
        size = random.randint(1,50)
        gene = ""
        for i in range(0,size,1):
            gene+=random.choice(self.instructions)
        return gene
    

    
    def run(self, generations=1000):
        """
            Evolve for a specified number of generations
        """
        gcount = 0
        
        while gcount<=generations:
            try:
                print "Gen: "+str(gcount),
                self.population = zip (self.population, [self.target]*len(self.population))
                self.population = self.pool.map(f, self.population)
            except:
                pass
            for i in self.population:
                print i[0],i[1]
            self.population = [organism.Organism(x[0], x[1]) for x in self.population]
            self.population.sort()
            print " Max fitness: "+str(self.population[::-1][1].fitness)
            try:
                if self.population[0] <= self.ppop[0]:
                     self.ppop = self.population[::-1][0:10] # The top ten organisms
                else:
                     self.population = self.ppop # We got worse! go back!
            except:
                self.ppop = self.population
            self.population = self.population[::-1][0:10]
            try:
                self.breed()
            except:
                print "Breeding error"
            gcount+=1
            
        
