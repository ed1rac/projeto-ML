# Exercício prático - Primeiro projeto de IA usando ML

1.  criar a pasta `projeto-ml-01`
2.  configurar o ambiente de programação
    1.  instalar o `poetry` (gerenciamento de dependências das bibliotecas e do ambiente virtual)
        1.  `pip install poetry`
        2.  Caso não consiga instalar o poetry use a página no Notion
    2.  depois, basta fazer: `poetry new projeto-ml-01`
        1.  O poetry, por padrão, cria o ambiente virtual em uma pasta global (no caminho \~/AppData/Local/pypoetry/Cache/virtualenvs/). No entanto, você pode configurar o poetry para criar o ambiente virtual na pasta do projeto onde você está.
        2.  Para definir isso como padrão global (ou seja, para todos os projetos), você pode configurar o poetry para criar o ambiente virtual no diretório do projeto usando o seguinte comando: 3.
        3.  `poetry config virtualenvs.in-project true`
        4.  Esse comando cria uma configuração que diz ao poetry para criar o virtual environment na pasta .venv dentro do próprio projeto, ao invés da pasta global.
        5.  A pasta do virtual environment será criada no próprio diretório do projeto, facilitando o gerenciamento local.
        6.  Depois de definir essa configuração, qualquer novo ambiente virtual criado pelo poetry será armazenado na pasta .venv do projeto atual.
    3.  entra na pasta (`cd projeto-ml-01`) e faz: `poetry shell` (isso vai criar o virtualenv para o projeto)