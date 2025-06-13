# Gerenciador de Estoque de Roupas

git remoto adicionar origem https://github.com/PedroAlmeida232/GerenciadorEstoque.git
 git branch -M main 
git push -u origin main

## Funcionalidades

- Dashboard com visão geral do estoque
- Gerenciamento de produtos e categorias
- Controle de entrada e saída de produtos
- Diferentes níveis de acesso:
  - Usuário Padrão: Pode apenas realizar saídas de produtos
  - Gerente: Pode realizar entradas e saídas de produtos
  - Superior: Pode adicionar novos produtos e categorias, além de realizar entradas e saídas

## Requisitos

- Python 3.8 ou superior
- Django 5.2 ou superior

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd gerenciador-estoque
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install django
```

4. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Configure os grupos e usuários:
```bash
python setup.py
```

## Usuários Padrão

O sistema vem com os seguintes usuários pré-configurados:

- **Usuário Padrão**
  - Usuário: `usuario`
  - Senha: `usuario123`

- **Gerente**
  - Usuário: `gerente`
  - Senha: `gerente123`

- **Superior**
  - Usuário: `superior`
  - Senha: `superior123`

- **Administrador**
  - Usuário: `admin`
  - Senha: `admin123`

## Executando o Sistema

1. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

2. Acesse o sistema em seu navegador:
```
http://localhost:8000
```

## Estrutura do Projeto

- `estoque/`: Aplicativo principal
  - `models.py`: Definição dos modelos
  - `views.py`: Lógica de negócios
  - `urls.py`: Configuração de URLs
  - `templates/`: Templates HTML
- `gerenciador_estoque/`: Configurações do projeto
- `setup.py`: Script de configuração inicial

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push -u origin main`)
5. Abra um Pull Request 