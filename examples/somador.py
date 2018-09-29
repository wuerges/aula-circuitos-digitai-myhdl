from myhdl import block, delay, always, always_comb, instance, now, Signal

# Explicação para as funções deste exemplo podem ser encontradas em:
# http://docs.myhdl.org/en/stable/manual/intro.html

@block
def Somador(a, b, c):

    @always_comb
    def do_sum():
        c.next = a + b
    return do_sum

@block
def TestBench():

    a = Signal(0)
    b = Signal(0)
    c = Signal(0)

    somador = Somador(a, b, c)

    @instance
    def do_test():
        a.next = 3
        b.next = 2
        yield delay(1)
        a.next = 7
        b.next = 10
        print("Verificando que c == 5")
        assert(c == 5)

        yield delay(1)
        print("Verificando que c == 17")
        assert(c == 17)
        a.next = 2
        b.next = 2

        print("Esperado um erro, pois c == 4")
        assert(c == 3)

    return somador, do_test


inst = TestBench()
inst.run_sim(30)
