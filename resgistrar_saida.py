def registrar_saida(conexao, id_produto, quantidade_saida):
    """Remove uma quantidade específica do estoque, validando se há saldo disponível."""
    cursor = conexao.cursor()
    
    cursor.execute("SELECT nome, quantidade FROM produtos WHERE id = ?", (id_produto,))
    produto = cursor.fetchone()
    
    if not produto:
        return "❌ Produto não encontrado!"
    
    nome_produto, qtd_atual = produto
    
    if quantidade_saida > qtd_atual:
        return f"❗Estoque insuficiente! Saldo atual de '{nome_produto}': {qtd_atual} unidades."
    
    nova_qtd = qtd_atual - quantidade_saida
    
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_qtd, id_produto))
    conexao.commit()
    
    alerta = ""
    if nova_qtd <= 5:
        alerta = f"\n❗ ATENÇÃO crítico: O produto '{nome_produto}' atingiu o estoque baixo ({nova_qtd} unidades)!"
        
    return f"✔️ Saída registrada! Estoque de '{nome_produto}' reduziu de {qtd_atual} para {nova_qtd}.{alerta}"