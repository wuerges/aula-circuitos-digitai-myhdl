from myhdl import block, delay, always, always_comb, instance, now, Signal


# Explicação para as funções deste exemplo podem ser encontradas em:
# http://docs.myhdl.org/en/stable/manual/intro.html

@block
def TestBench():

    @instance
    def do_test():
        while True:
            yield delay(1)
            print("passou 1 unidade de tempo.")

    return do_test

inst = TestBench()
inst.run_sim(30)
