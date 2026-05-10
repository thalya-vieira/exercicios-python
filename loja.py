#     3. Sistema de Controle de Vendas Uma loja precisa registrar vendas diárias. Desafio:
# Criar um sistema que:
#         ◦ Registre produto e valor
#         ◦ Some total vendido no dia
#         ◦ Mostre maior venda realizada


print("\n=== Vendas do dia ===")
vendas = {}
total_vendido = 0
maior_venda = 0



while True:
    
    registrar = input("\nRegistrar venda? s/n : ")
    
    # quero registrar venda
    if (registrar == "s" or registrar == "S"):
        produto = input("Nome do produto: ")
        valor = float(input("Valor do produto: "))

        vendas[produto] = {
            "valor" : valor
        }

        # soma de venda
        total_vendido += valor

        # maior venda
        if (maior_venda<valor):
            maior_venda = valor
            produto_maior_venda = produto

        print("Venda registrada!")

    # nao quero registrar venda
    elif (registrar == "N" or registrar == "n"):

        print("\n=== RESUMO DO DIA ===")

        print("Total vendido: R$", total_vendido)

        if len(vendas) > 0:
            print("\nMaior venda:")
            print("-Produto:", produto_maior_venda)
            print("-Valor: R$", maior_venda)  


        print("Programa finalizado")
        break

    else:
        print("Opcao invalida")

        



