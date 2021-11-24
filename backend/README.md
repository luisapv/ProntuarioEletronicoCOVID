# ProntuarioEletronicoCOVID
O prontuário eletrônico com foco no tramento e coleta de informações de pacientes diagnosticados com COVID-19.

A pandemia do COVID-19 propiciou uma aceleração do uso de tecnologias que permitam que a sociedade interaja de forma remota. Nosso projeto, o ProntuarioEletronicoCOVID consiste em um sistema que utilize API's e Webservice escrito em Python para que médicos possam ter acesso e compartilhar informações bem como realizar o acompanhamento do tramento ou evolução do quadro infeccioso e seus sintomas provendo análise de forma invidualizada além contar com dados pessoais que podem ser anomizados criando uma base de conhecimento que pode ser aproveitada em metodologia clínica de forma estatística. O ProntuarioEletronicoCOVID suportará campos para armazenar ainda dados descritivos, receituário médico, armazenamento de arquivos com resultados de exame e contará com uma funcionalidade de forum padrão de mercado para possibilitar a troca de informações diretas entre paciente e médico.

O sistema é desenvolvido, documentado e implementado pelos alunos do GRUPO10 da UnigranRio da turma de PCA: SISTEMAS DE INFORMAÇÃO DISTRIBUIDA:

# Colaboradores

Luis Alfredo Pacheco do Vale | https://github.com/luisapv

Leonardo Casteliano de Oliveira | https://github.com/iiPr0s

Jonas Israel Anselmé Vila Nova  | https://github.com/jiavn

José Vítor Cruz de Souza | https://github.com/vitorcruzfaculdade

# BackEnd em Python
Este projeto é uma atividade voltada à graduação de Ciências da Computação da universidade Unigranrio. Este trabalho foi dividido em frontend e backend. Aqui está o código do backend do projeto feito em Python com Flask e usando um banco de dados relacional. Durante o desenvolvimento foi utilizado SQLite, porém com alteração da string de conexão com o banco de dados é possível utilizar qualquer banco de dados relacional, tais como: PostgreSQL, OracleDB e etc.
## Dependências
Aqui estamos utilizando o `python3.9.0`, assim, certifique-se de que esta versão esteja instalada e disponível para ser utilizada.
Caso não tenha esta versão instalada, pode ser feito o download [nesta página](https://www.python.org/downloads/release/python-397/).

Este projeto utiliza as bibliotecas
- virtualenv
- flask
- python-dotenv
- sqlalchemy
- flask-sqlalchemy

A biblioteca ___virtualenv___ é utilizada para criar ambientes virtuais que isolam o código e suas dependências da instalação padrão do Python de maneira que não comprometa o funcionamento de outras aplicações. 

A biblioteca ___python-dotenv___ é utilizada para carregar configurar e carregar variáveis de ambiente, normalmente descritas no arquivo ___.env___, porém aqui no repositório este arquivo não está presente pois constitui grave falha de desenvolvimento.

As bibliotecas ___sqlalchemy___ e ___flask-sqlalchemy___ são ORM (Object Relational Mapper) que vão ser responsáveis por conectar ao banco de dados, criar o database, criar e popular as tabelas e fazer o mapeamento das classes que descrevem os modelos com suas respectivas tabelas. Esse modelo segue as boas práticas pois evita que o usuário interaja diretamente com o banco de dados, o que é uma grave falha de segurança no desenvolvimento. 

A biblioteca flask é um microframework para desenvolvimento web. Aqui ele será responsável por criar uma API que será consumida pelo frontend.

## Instalação
Com o `python3.9` instalado e com os arquivos do repositório prontos, basta abrir o terminal na pasta ___root___ do projeto e seguir os próximos passos.

### Criando um ambiente virtual
Primeiramente instale o módulo ___virtualenv___ do python com o comando `pip install virtualenv`, assim será possível utilizar este módulo para criar o ambiente virtual.

Assim que a instalação estiver finalizada, execute o comando `virtualenv .<nome do ambiente virtual>`, exemplo `virtualenv .venv`.

Assim que o ambiente virtual estiver criado, faltará ativá-lo. Dependendo do seu sistema operacional, o comando é diferente.

#### Ativando o ambiente virtual no Windows
No Windows, existe um script chamado ___activate___ no path _.\\.\<nome do ambiente virtual\>\\Scripts\\activate_. Vamos utilizar como exemplo o ambiente virtual `.myenv`. Assim é possível ativar o ambiente virtual de duas formas:

1. `$cd .myenv\Scripts\`
e após o terminal estar no diretório em questão, utilizar o comando `.\activate`. Se estiver utilizando o prompt de comando, será possível ver no início da linhas de comando o nome do ambiente virtual `(.myenv)`, isso indica que o ambiente virtual está ativado.
2. `.\myenv\Scripts\activate` e então o ambiente virtual deve se ativar.

#### Ativar o ambiente virtual no Linux ou no Mac
No Linux e no Mac o processo é igual. Vamos considerar o ambiente virtual `.myenv`. Assim é possível ativar o ambiente virtual de duas formas:

1. `$cd .myenv/bin/`
e após o terminal estar no diretório em questão, utilizar o comando `source ./activate`. Se estiver utilizando o bash, será possível ver no início da linhas de comando o nome do ambiente virtual `(.myenv)`, isso indica que o ambiente virtual está ativado.
2. `source ./myenv/bin/activate` e então o ambiente virtual deve se ativar.

### Instalando as dependências
Com o ambiente virtual ativado, basta executar o comando `pip install -r requirements.txt`. Certifique-se de que o terminal está sendo executado na pasta root do projeto.

O módulo pip vai identificar as dependências, baixar os arquivos necessários para a instalação e instalá-los na pasta do ambiente virtual.

## Executando o projeto
Com o ambiente virtual ativado e as dependências instaladas, basta abrir o terminal na pasta root do projeto e executar o comando `python main.py` e o python executará o flask e será possível interagir com ele.