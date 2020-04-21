Há diversas formas de gerar um executável em python. Para este projeto utilizamos o *pyinstaller*, sendo chamado pelo *command prompt* do Windows.
A instalação mais comum do python é usando a distribuição Anaconda (https://www.anaconda.com/distribution/). Todavia, observamos que o executável gerado com o Anaconda é muito pesado, porque durante a geração do executável são importados diversos pacotes desnecessários, que são padrão do Anaconda. 

Os passos que seguimos, então, para gerar o executável para este projeto são os seguintes:

1. Instalação do python (https://www.python.org/downloads/windows/). Importante escolher a arquitetura correta (64bits, correspondente a máquina do cliente), pois talvez o executável gerado não funcione caso escolha a arquitetura errada.

2. Depois da instalação o python é chamado via *command prompt* do Windows. Primeiramente, precisamos instalar o *pip* (pacote que permite instalar outros pacore no python). Chame o *command prompt* e digite:

```python
>>> python get-pip.py
```

3. Depois instale os pacotes necessários do projeto via pip, inclusive o pyinstaller:

```python
>>> pip install pyinstaller
```

4. Navegue até o diretório do projeto:

```python
>>> cd diretorio_do_projeto
```

5. Finalmente, para gerar o executável usamos a seguinte linha de comando:

```python
>>> pyinstaller --onefile gui\interface.py
```
onde a flag *--onefile* permite gerar o executável em um único arquivo. São criadas duas pastas: *build* e *dist*. O executável estará na pasta *dist*. Mova o arquivo executável para a pasta raiz do projeto e ele já estará pronto para ser executado. 
