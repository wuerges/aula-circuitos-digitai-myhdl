
# Instalando o myhdl

Para instalar o myhdl, é necessário primeiro instalar o python 3.6. Confira a versão do seu python:

```
$ python --version
Python 3.6.6
```
De posse do python 3.6, basta instalar o myhdl usando o pip, ou o pipenv (minha sugestão).

```
$ pipenv --python 3.6
$ pipenv install myhdl
$ pipenv run python
```
Este link mostra o procedimento: https://asciinema.org/a/bi8438DoT8lGN523YVTBCJIF8

# Usando o myhdl

O myhdl funciona como uma biblioteca do python. Basta importá-lo no arquivo, como está nos exemplos.

## Criando um testbench

O arquivo [examples/testbench.py](examples/testbench.py) é um exemplo de testbench:


```python
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
```

O decorador @block transforma a função Somador em um circuito digital.
O decorador @instance adiciona um comportamento ao bloco.
O yield delay(1) cria um evento de passagem de tempo. Isto é, quando é executado, o tempo passa 1
unidade de tempo.

__Atenção:__ o uso do decorador @instance impede que o circuito seja sintetizável.

## Executando o TestBench

Para executar o testbench, basta invocar o arquivo com o python: https://asciinema.org/a/rHSuijCDMDFdaU3FSBprIDyi4

```
$ python examples/testbench.py
```

## Criando um circuito combinacional

O arquivo [examples/somador.py](examples/somador.py) é um exemplo de circuito combinacional,
em conjunto com um testbench.

O circuito combinacional é descrito pelo seguinte trecho:

```python
@block
def Somador(a, b, c):

    @always_comb
    def do_sum():
        c.next = a + b
    return do_sum
```
O decorador @block transforma a função Somador em um circuito digital.
O decorador @always_comp transforma a função do_sum em uma função combinacional.

A função _do_sum_ realiza a soma dos valores _a_ e _b_ e atribui ao _c_.
Porque os valores são lidos de  _a_ e _b_, eles serão considerados __entradas__.
Porque o valor de _c_ é atribuído, ele será considerado uma __saída__.


O seguinte trecho mostra um testbench criado para testar o Somador.

```python
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
```

Para o testbench poder interagir com o circuito Somador é necessário criar sinais
para atribuir as duas entradas e a saída do circuito.

Sinais são criados usando a função Signal, que recebe por parâmetro o valor inicial do sinal.

O circuito somador é criado dentro do testbench, e recebe os sinais como parâmetro.

A função do_test, com o decorador @instance, implementa o comportamento do testbench.
Perceba que o valor de _c_ se modifica quando os valores de _a_ e _b_ são alterados, somente após a passagem de uma unidade de tempo.

## Testando o circuito combinacional

O circuito é testado, executando seu testbench: https://asciinema.org/a/Fu6DHZQDpTomRXKuUh9Xfw5vM

```
$ python examples/somador.py
```
