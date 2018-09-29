
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

O arquivo [examples/testbench.py](examples/testbench.py) é um exemplo de testbench.
O tesbench é um circuito sequencial não sintetizável, porque usa uma _instance_.

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
