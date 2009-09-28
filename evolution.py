import organism
import random

class EvolutionError():
    pass

class Evolution():
    """
        Provides an environment for our litte bf organisms to evolve in.
    """
    def __init__(self, pop_size=None, target=None):
        """
            Set up the environment and a default population of pop_size
        """
        if (target == None or pop_size==None):
            raise EvolutionError("Must specify BOTH pop_size and a target")
        self.population = []
        self.ppop = None
        self.instructions = (">","<","+","-","[","]")
        self.pop_size = pop_size
        self.target = target
        # Now seed a random population
        while (len(self.population) <= self.pop_size):
            self.population.append(organism.Organism(self.random_gene()))
     
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
            print "Gen: "+str(gcount),
            for org in self.population:
                org.evaluate(self.target)
            self.population.sort()
            print " Max fitness: "+str(self.population[::-1][1].fitness)
            try:
                if self.population[0] >=self.ppop[0]:
                     self.ppop = self.population[::-1][0:10] # The top ten organisms
                else:
                     self.population = self.ppop # We got worse! go back!
            except:
                self.ppop = self.population
            self.population = self.population[::-1][0:10]
            self.breed()
            gcount+=1
            
        
