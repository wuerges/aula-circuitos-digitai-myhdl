from myhdl import block, delay, always, now

# Explicação para as funções deste exemplo podem ser encontradas em:
# http://docs.myhdl.org/en/stable/manual/intro.html

@block
def HelloWorld():

    @always(delay(10))
    def say_hello():
        print("%s Hello World!" % now())

    return say_hello


inst = HelloWorld()
inst.run_sim(30)
