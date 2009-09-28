import evolution

evolver = evolution.Evolution(500,[1,1,2,6,24,120,720,5040,40320,362880,3628800])
try:
    evolver.run(10)
except:
    print "Some form of error"
    pass
evolver.population.sort()# Best of the best :-p
print evolver.population[::-1][0]
