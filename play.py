import bfinterpreter

bfi = bfinterpreter.BFInterpreter()
bfi.preprocess_program("->-<[>[]+]<[]-+>]>-][]->++<[+>-+-+[---+--<+-+]+<+->]+>>>>-+--[>[]><[><]<>]>-<+-<-<<++>]]]<+>[]><]>><+++>>[[<<<>[>-]+>[+-[--[++[->-[->+[>[--]---")
bfi.execute()
