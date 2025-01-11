# Sistema de Vendas e Controle de Estoque

Este é um sistema desenvolvido em Django para gerenciar vendas, controle de estoque, relatórios financeiros e cadastro de usuários. O projeto oferece funcionalidades como gestão de produtos, fornecedores, clientes e relatórios detalhados de vendas.

## Recursos do Projeto

1. **Autenticação de Usuários**:
   - Sistema de login e registro com suporte a diferentes níveis de hierarquia (usuário, administrador).

2. **Gestão de Vendas**:
   - Cadastro de vendas com seleção de produtos.
   - Cálculo automático do valor total da venda.
   - Relatório detalhado por produto e método de pagamento.

3. **Controle de Estoque**:
   - Atualização automática do estoque após cada venda.
   - Alertas para produtos com baixo estoque.

4. **Gestão de Produtos e Fornecedores**:
   - Cadastro, edição e exclusão de produtos.
   - Cadastro de fornecedores vinculados aos produtos.

5. **Relatórios Financeiros**:
   - Total de vendas por produto.
   - Relatórios de receita total por método de pagamento.

## Tecnologias Utilizadas

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript
- **Banco de Dados**: SQLite (padrão, mas compatível com MySQL)
- **Bibliotecas**:
  - `django-crispy-forms` para formatação de formulários.
  - `chart.js` para visualização de dados em gráficos.

## Configuração do Projeto

### Requisitos
- Python 3.9+
- Pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:
   ```bash
    git clone -b rafael_develop https://github.com/bkfantasma/estoque.git
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Login de Teste:
   ```
   email: tester@tester.com
   senha:tester
   ou cadastre um novo usuario
   ```


Acesse o sistema em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Estrutura do Projeto

```
.
├── core
├── estoque
├── fornecedores
├── produto
├── user
├── vendas
└── templates
```

- **core**: Módulo central com configurações gerais.
- **estoque**: Gerenciamento de estoque e produtos com baixo estoque.
- **fornecedores**: Cadastro de fornecedores vinculados aos produtos.
- **produto**: Gestão de produtos e categorias.
- **user**: Sistema de autenticação e hierarquia de usuários.
- **vendas**: Controle de vendas, relatórios e cálculo de totais.
- **templates**: Arquivos HTML para renderização das páginas.

## Funcionalidades Planejadas
- Relatórios personalizados.
- Integração com APIs de pagamento.
- Suporte a múltiplos idiomas.
