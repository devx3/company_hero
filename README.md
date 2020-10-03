# Company Hero API

Essa é uma API criada para um teste da [Company Hero](https://www.companyhero.com/)

Esse foi um projeto muito divertido e que com certeza me agregou muito! 

Então vamos a configuração.

## INFORMAÇÕES SOBRE O PROJETO:


## PONTA PÉ INICIAL

Antes de começarmos, você pode conferir uma DEMO da aplicação clicando [aqui](https://companyhero.herokuapp.com/)

Você pode acessar a área administrativa da aplicação [aqui](https://companyhero.herokuapp.com/).

- **Login:** admin
- **pass:** 123456

Para de fato utilizar a API, eu criei uma documentação que você pode e deve estar acessando clicando [aqui](https://linkhere.com). 

## CONFIGURAÇÃO DA API DO ZERO

Agora que você já conferiu a demo a API, podemos começar com o tutorial de configuração dessa API no seu próprio servidor, caso queira.

### CLONANDO PROJETO

`https://github.com/devx3/company_hero.git`

### INSTALANDO DEPENDÊNCIAS
Por estarmos utilizando o Django, temos algumas dependências que precisamos instalar para que tudo funcione 100%. 

Acesse a pasta do projeto: 
`cd company_hero`

E então execute o comando para instalar as dependências:
`python3 -m pip install -r requirements.txt`

Ou se o PIP estiver configurado no seu PATH:

`pip install -r requirements.txt`

### CONFIGURAÇÃO DO DJANGO

Configurar o django é bem simples, primeiro precisamos migrar os nossos models para que seja criado as tabelas na base dados:

`python manage.py migrate`

Depois disso, é necessário criar um super usuário e gerar o Token de acesso para ele

Digite: 
`python manage.py createsuperuser`

Preencha os seus dados. 

### GERANDO TOKEN DE ACESSO

Aqui você vai precisar acessar a sua área administrativa para gerar seu token. 

Acesse: http://seudominioconfigurado.com/admin

[IMAGEM AQUI]

Preencha o seu **username** e **senha** que você acabou de criar para acessar o painel do sistema. 

Depois de logado, vá na seção "TOKEN DE AUTENTICAÇÃO" e clique em Tokens. 

[IMAGEM AQUI]

Nessa tela você terá a listagem de todos os tokens gerados para a sua aplicação. 

Clique no botão **ADICIONAR TOKEN** no canto superior direito.

[IMAGEM AQUI]

Na tela seguinte, basta você selecionar o usuário que você acabou de criar e clicar em Salvar. 

Pronto! Será gerado um token para o seu usuário. Guarde esse token com segurança!

[IMAGEM AQUI]

Agora que você já possui um Token de Acesso, você já pode utilizar a API.

Clique aqui para acessar a documentação da API. 

### CONCLUSÃO

Agora, você já tem a aplicação rodando e com o seu token de acesso. Deixe a imaginação fluir e integre esse API com O QUE VOCÊ QUISER! 

Cheers & Happy Code! 