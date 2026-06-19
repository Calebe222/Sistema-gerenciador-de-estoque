# Sistema de Estoque

Aplicação desktop simples para gerenciar produtos e vendas usando Tkinter e PostgreSQL.

## Recursos
- Cadastro, edição e remoção de produtos
- Registro de vendas e atualização de estoque
- Visualização de estoque e histórico de vendas

## Requisitos
- Python 3.8+
- PostgreSQL
- Dependências Python: `psycopg2-binary`, `Pillow`, `python-dotenv` (opcional)

Instale dependências:
```bash
pip install -r requirements.txt
# ou manualmente
pip install psycopg2-binary Pillow python-dotenv
```

## Configuração
1. Configure seu banco PostgreSQL (host, database, user, senha).
2. Para não commitar credenciais, use variáveis de ambiente ou um arquivo `.env` (não comitado).

Exemplo de `.env` (não comitar):
```
DB_HOST=localhost
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=sua_senha_aqui
```

No `main.py` o código já tenta usar variáveis de ambiente se presentes.

## Como rodar
1. No diretório do projeto:
```bash
python main.py
```

## Estrutura do banco (observações)
- A tabela `produtos` usa colunas: `id`, `nome`, `quantidade` (ou `qtde`), `preco`.
- A tabela `vendas` usa colunas: `id`, `nomevenda` (ou `nomeVenda`), `qtde`, `precototal`, `data`.

O projeto tenta detectar nomes de colunas comuns (`qtde` ou `quantidade`) automaticamente.

## Imagens
Coloque imagens (`wallpaper.png`, `logo.png`, `logo2.png`) na mesma pasta do projeto se preferir não usar o caminho `Projetos/Sistema de Estoque/...`.

## GitHub / Segurança
- Não comite senhas. Adicione `.env` ao `.gitignore`.
- Se já comitou uma credencial, rotacione a senha e remova o segredo do histórico (use BFG ou `git filter-repo`).