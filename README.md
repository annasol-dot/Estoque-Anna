# Estoque-Anna

Sistema criado para gestão de estoque de diversos produtos, desenvolvido em python utilizando o banco de dados relacional sqlite3. O sistema permite o cadastro de produtos, registrar entrada e saída (adicionar e remover) e consulta de estoque.


# Funcionalidades

- Cadastro de produtos
   - Permite cadastrar o nome do produto, categoria, quantidade inical e preço. O ID é gerado automaticamente para o produto.
- Registrar entrada e saída
   - Adiciona ou remove produtos do estoque. Para remover existe uma validação para que o estoque não fique negativo.
- Consultar estoque por ID
   - Com o ID gerado, é possivel consultar o estoque, vendo o nome do produto, seu preço e sua quantidade.
- Alerta de estoque baixo
   - O sistema monitora constantemente os níveis do estoque. Se um produto atingir **5 unidades ou menos**, um alerta visual crítico é disparado imediatamente na tela.


# Acesso pelo colab 
https://colab.research.google.com/drive/1NLTDvaPj6MKvZTmfsAKzOQNecZcA7v84?usp=sharing
