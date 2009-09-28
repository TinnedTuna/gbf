import unittest
import organism

class TestOrganism( unittest.TestCase ):
    def setUp(self):
        pass
    
    def testSimple(self):
        """
            Test that the organism can run.
        """
        code = "++++"
        org = organism.Organism(code)
        org.evaluate([4,0,0,0,0,0,0,0,0,0])
        self.assertEqual(3.0, org.fitness)
        
    def testComparison(self):
        """
            Test that a 'better' organism is indeed the one that comes out
            on top of a comparison.
        """
        good_code= "+++++"
        bad_code = "++++"
        good_org = organism.Organism(good_code)
        bad_org = organism.Organism(bad_code)
        target = [5,0,0,0,0,0,0,0,0,0]
        good_org.evaluate(target)
        bad_org.evaluate(target)
        self.assert_(good_org > bad_org)
        
    def testSorting(self):
        """
            Test that an obviously good organism comes top in a sorted list.
        """
        target = [100,0,0,0,0,0,0,0,0,0]
        organisms = []
        code = ""
        for i in range(1,90,1):
            code+="+"
            organisms.append(organism.Organism(code))
        for org in organisms:
            org.evaluate(target)
        organisms.sort()
        #print organisms[::-1][0], len(organisms[::-1][0].code)
        self.assertEqual(89, len(organisms[::-1][0].code))
        
        
    def testGoodVsFailed(self):
        """
            Ensure that viable organisms will be favoured over non-viable
        """
        target = [4,0,0,0,0,0,0,0,0,0]
        bad_code = ["+++<",  # Tape underflow
                    "+[<]", # Tape underflow
                    "+-+->><<<", # Tape underflow
                    "+[+]", # Time exceeded
                    "+[>>>>>>>>>>>>>+]", # Memory exceeded
                    ]
        good_code = ["+","++","++[>++<-]>[<+>-]","++++","+++"]
        organisms=[]
        for code in bad_code:
            organisms.append(organism.Organism(code))
        for code in good_code:
            organisms.append(organism.Organism(code))
        for org in organisms:
            org.evaluate(target)
        organisms.sort()
        self.assert_(organisms[0].code in good_code)  # 2 is actually the "best"
                                                   # balance of correctness
                                                   # and length