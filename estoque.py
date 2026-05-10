# 1.	Controle de Estoque de Papelaria
# Uma papelaria possui dificuldades para controlar entradas e saídas de produtos.
# Desafio:
# Criar um sistema em Python que:
# •	Cadastre produtos
# •	Informe quantidade em estoque
# •	Atualize entradas e vendas
# •	Mostre produtos com estoque baixo


estoque = {}
while True:
    
    print("\n===controle de estoque===")
    print("1. Adicionar produto")
    print("2. Mostrar estoque")
    print("3. Entrada")
    print("4. Saída")
    print("5. Sair")
 
    opcao = input("Opção: ")
    match opcao:
        case "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))

            estoque[nome] = {
                "quantidade": quantidade,
            }
            print("Produto adicionado!")

        case "2": 
            if len(estoque) == 0:
                print("Estoque vazio.")
            else:
                for produto, dados in estoque.items():
                    print("-"*30)
                    print("Produto:", produto)
                    print("Quantidade:", dados["quantidade"])
        
        case "3": 

            nome = input("Produto para entrada: ")
            if nome in estoque:

                quantidade = int(input("Quantidade de entrada: "))

                estoque[nome]["quantidade"] += quantidade

                print("Entrada realizada!")
            else:
                print("Produto não encontrado.")

        case "4": 

            nome = input("Produto para saída: ")
            if nome in estoque:
                quantidade = int(input("Quantidade de saída: "))

                if estoque[nome]["quantidade"] >= quantidade:


                    estoque[nome]["quantidade"] -= quantidade

                    print("Saída realizada!")
                else:
                    print("Estoque insuficiente.")
            else:
                print("Produto não encontrado.")

        case "5":
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida.")