import sqlite3

def conectar_banco():
    """Estabelece a conexão com o banco de dados e cria a tabela se não existir."""
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    
 
    cursor.execute("DROP TABLE IF EXISTS produtos")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conexao.commit()
    return conexao