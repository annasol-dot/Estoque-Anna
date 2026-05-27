def registrar_entrada(conexao, id_produto, quantidade_entrada):
    """Adiciona uma quantidade específica ao estoque de um produto existente."""
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome, quantidade FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()
    
    if not produto:
        return "❌ Produto não encontrado!"
    
    nome_produto, qtd_atual = produto
    nova_qtd = qtd_atual + quantidade_entrada
    
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_qtd, id_produto))
    conexao.commit()
    
    alerta = ""
    if nova_qtd <= 5:
        alerta = f"\n⚠️ ATENÇÃO: O produto '{nome_produto}' ainda está com estoque baixo ({nova_qtd} unidades)!"
        
    return f"✔️ Entrada registrada! Estoque de '{nome_produto}' subiu de {qtd_atual} para {nova_qtd}.{alerta}"

