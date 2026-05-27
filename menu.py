def menu_principal():
    conn = conectar_banco()
    
    while True:
        print("\n==============================")
        print("--- MENU DO ESTOQUE ---")
        print("==============================")
        print("1. Cadastrar Produto")
        print("2. Resgistrar Entrada")
        print("3. Resgistrar Sáida")
        print("4. Consultar Produto por ID")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == "1":
            print("\n--- CADASTRO DE PRODUTO ---")
            nome = input("Nome do produto: ")
            categoria = input("Categoria: ")
            qtd = int(input("Quantidade inicial: "))
            preco = float(input("Preço unitário: "))
            
            resultado = cadastrar_produto(conn, nome, categoria, qtd, preco)
            print(resultado)
            
        elif opcao == "2":
            print("\n--- ADICIONAR PRODUTO ---")
            id_p = int(input("Digite o ID do produto: "))
            qtd = int(input("Quantidade a ser adicionada: "))
            
            resultado = alterar_quantidade(conn, id_p, qtd, "adicionar")
            print(resultado)
            
        elif opcao == "3":
            print("\n--- REMOVER PRODUTO ---")
            id_p = int(input("Digite o ID do produto: "))
            qtd = int(input("Quantidade a ser removida: "))
            
            resultado = alterar_quantidade(conn, id_p, qtd, "remover")
            print(resultado)
            
        elif opcao == "4":
            print("\n--- CONSULTAR PRODUTO ---")
            id_p = int(input("Digite o ID do produto: "))
            
            resultado = consultar_produto(conn, id_p)
            print(resultado)
            
        elif opcao == "5":
            print("\nEncerrando o sistema... Até logo!")
            conn.close()
            break #Quebra o loop encerrando o programa
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()
