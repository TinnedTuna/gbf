import evolution

# Some inital starting organisms
good_codes = [
              "+",
              "+>+",
              "+>+>++",
              "+[>+<-]",
              "+[>+>+<<-]",
              "+[>+>+<<-]>>[<<+>>-]",
              "+>++>++++++",
              "++>++>+++>++++++"
              ]
evolver = evolution.Evolution(50,[1,1,2,6,24,120,720,5040,40320,362880,3628800], good_codes)
try:
    evolver.run(1000)
except:
    print "Some form of error"
    pass
evolver.population.sort()# Best of the best :-p
print evolver.population[::-1][0]
