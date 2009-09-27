import evolution

evolver = evolution.Evolution(50000,[1,1,2,6,24,120,720,5040,40320,362880,3628800])
try:
    evolver.run(1000)
except:
    print "Some form of error"
    pass
print evolver.population[0] # Best of the best :-p
