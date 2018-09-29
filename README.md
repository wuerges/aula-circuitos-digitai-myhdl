
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

O arquivo (examples/testbench.py) é um exemplo de testbench.
O tesbench é um circuito sequencial não sintetizável, porque usa uma _instance_.
