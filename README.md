# Company Hero API

Essa é uma API criada para um teste da [Company Hero](https://www.companyhero.com/)

Esse foi um projeto que eu me senti muito feliz em executar. Além de me divertir muito, eu procurei absorver o máximo de conhecimento possível!


Bora pra configuração! 

## BRIEFING DO PROJETO: 
Eu como Dev Frontend na Company Hero, gostaria criar empresas com um formulário simples. Preciso saber quais dados enviar em JSON e para qual URL. A ideia é criar um diretório de empresas e seus funcionários, estos funcionários seriam os usuários da plataforma porem precisamos considerar que um usuário pode pertencer a mais de uma empresa.

Depois de criada a empresa e os usuário preciso de um endpoint para trazer todas as informações da empresa e seus usuários e outro endpoint para trazer um usuário pelo seu username e saber a qual ou quais empresa ele pertence.

## INFORMAÇÕES SOBRE O PROJETO:

- Python Version: 3.7.5
- Django Version: 3.1.9
- Django Rest Framework Version: 3.12.1

## PONTA PÉ INICIAL

Antes de começarmos, você pode conferir uma DEMO da aplicação clicando [aqui](https://companyhero.herokuapp.com/)

Você pode acessar a área administrativa da aplicação [aqui](https://companyhero.herokuapp.com/admin).

- **Login:** admin
- **pass:** 123456

Para de fato utilizar a API, eu criei uma documentação que você pode e deve acessar clicando [aqui](https://documenter.getpostman.com/view/7747875/TVRg699E). 

## CONFIGURAÇÃO DA API DO ZERO

Agora que você já deu uma olhada na demo da API, podemos começar com o tutorial de configuração no seu próprio servidor, caso queira.

### CLONANDO PROJETO

`git clone https://github.com/devx3/company_hero.git`

### INSTALANDO DEPENDÊNCIAS
Por estarmos utilizando o Django, temos algumas dependências que precisamos instalar para que tudo funcione 100%. 

Acesse a pasta do projeto: 

`cd company_hero`

E então execute o comando para instalar as dependências:

`python3 -m pip install -r requirements.txt`

Ou se o PIP estiver configurado no seu PATH:

`pip install -r requirements.txt`

### CONFIGURAÇÃO DO DJANGO

Primeiramente é necessário você gerar a sua SECRET_KEY e inserí-la na sua variável de ambiente. Por segurança essa informação não é inserida diretamente no settings.py. 

Para gerar a sua chave, abra um terminal e digite: 

- `python`
- `import secrets`
- `secrets.token_hex(24)`

Após esses passos, você terá um resultado parecido com o abaixo: 

`e10ac06ef8b23000c233b584ea46205f99f3b78ae581b384`

Se estiver ambiente shell, execute: 

`export SECRET_KEY="e10ac06ef8b23000c233b584ea46205f99f3b78ae581b384"`

Se estiver no windows, execute: 

`set SECRET_KEY="e10ac06ef8b23000c233b584ea46205f99f3b78ae581b384"`

Lembre-se que o comando para Windows criará essas variáveis TEMPORARIAMENTE no terminal ativo. Ou seja, assim que você fechar o console, essas variáveis serão excluídas. 

Para torná-la permanente, segue um tutorial para isso: 

https://devcontent.com.br/artigos/windows/o-que-sao-como-alterar-criar-excluir-variaveis-de-ambiente

Agora, precisamos alterar a variável DEBUG. 

### PARA AMBIENTE DE DESENVOLVIMENTO

Abra o arquivo `settings.py` dentro da pasta heroes e aqui você vai alterar duas variáveis.

A primeira é a DEBUG: 

Altere de:

`DEBUG = os.environ.get('DEBUG') == True`

para: 

`DEBUG = True`

e altere a variável `ALLOWED_HOSTS`. Para ambientes de teste, você pode deixar essa variável da seguinte forma: 

`ALLOWED_HOSTS = []`

### PARA PRODUÇÃO

Primeiro, defina a variável DEBUG como True.

Se estiver ambiente shell, execute: 

`export DEBUG="True"`

Se estiver no windows, execute: 

`set DEBUG="True"`

Abra o arquivo `settings.py` dentro da pasta heroes e altere a variável `ALLOWED_HOSTS` para: 

`ALLOWED_HOSTS = ['https://seudominioaqui.com']`

### MIGRAÇÕES

Configurar o django é bem simples, primeiro precisamos migrar os nossos models para que seja criado as tabelas na base de dados:

`python manage.py migrate`

Depois disso, é necessário criar um super usuário e gerar o Token de acesso para ele.

**Digite:** 

`python manage.py createsuperuser`

Preencha os seus dados. 

### GERANDO TOKEN DE ACESSO

Nessa etapa você vai precisar acessar a área administrativa. 

1. Acesse: http://seudominioconfigurado.com/admin
2. Preencha o seu **username** e **senha** que você acabou de criar para acessar o painel do sistema
3. Depois de logado, vá na seção **"TOKEN DE AUTENTICAÇÃO"** e clique em *Tokens*

Nessa tela você terá a listagem de todos os tokens gerados para a sua aplicação. 

4. Clique no botão **ADICIONAR TOKEN** no canto superior direito
5. Selecione o usuário que você acabou de criar e clique em Salvar
6. Feito! O seu token foi gerado e você deve guardá-lo em segurança

Agora que você já possui um Token de Acesso, você já pode utilizar a API.

[Clique aqui](https://documenter.getpostman.com/view/7747875/TVRg699E) para acessar a documentação da API. 

### CONCLUSÃO

Agora, você já tem a aplicação rodando e com o seu token de acesso. Deixe a imaginação fluir e integre esse API com O QUE VOCÊ QUISER! 

## Cheers & Happy Code! 
