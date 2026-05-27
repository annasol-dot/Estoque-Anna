def consultar_produto(conexao, id_produto):
    """Busca e exibe um produto específico pelo seu ID."""
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()
    
    if produto:
        id_p, nome, categoria, qtd, preco = produto
        
        info = f"\n--- PRODUTO ENCONTRADO ---"
        info += f"\nID: {id_p}"
        info += f"\nNome: {nome}"
        info += f"\nCategoria: {categoria}"
        info += f"\nQuantidade: {qtd}"
        info += f"\nPreço: R$ {preco:.2f}"
        
        if qtd <= 5:
            info += f"\n❗ ALERTA: Estoque crítico ({qtd} unidades)!"
            
        return info
    else:
        return "❌ Produto não encontrado."