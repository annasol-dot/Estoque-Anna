def cadastrar_produto(conexao, nome, categoria, quantidade, preco):
    """Cadastra um novo produto no banco de dados."""
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO produtos (nome, categoria, quantidade, preco)
        VALUES (?, ?, ?, ?)
    """, (nome, categoria, quantidade, preco))
    conexao.commit()
    return f"✔️ Produto '{nome}' cadastrado com sucesso!"