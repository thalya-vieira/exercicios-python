# # 2. Cadastro de Clientes para uma Clínica
# # Uma clínica deseja organizar o cadastro dos pacientes.
# # Desafio:
# # Desenvolver um programa que:
# #         Cadastre nome, idade e telefone
# #         Pesquise pacientes cadastrados
# #         Exiba lista organizada em ordem alfabética        

cadastro = {}

while True:
    print("\n=== Cadastro de Clientes ===")
    print("1. Adicionar cliente")
    print("2. Pesquisar cliente")
    print("3. Excluir cliente")
    print("4. Mostrar lista")
    print("5. Sair do programa")

    opcao = input("Opção: ")

    match opcao:

        case "1":
            cliente = input("Cliente: ")
            idade = int(input("Idade: "))
            telefone = input("Telefone: ")

            cadastro[cliente] = {
                "idade": idade,
                "telefone": telefone
            }

            print("Cliente adicionado com sucesso!")

        case "2":
            pesquisa = input("Qual cliente deseja pesquisar? ")

            if pesquisa in cadastro:
                dados = cadastro[pesquisa]

                print("\nCliente encontrado!")
                print("Nome:", pesquisa)
                print("Idade:", dados["idade"])
                print("Telefone:", dados["telefone"])

            else:
                print("Cliente não encontrado.")

        case "3":
            excluir = input("Qual cliente deseja excluir? ")

            if excluir in cadastro:
                del cadastro[excluir]
                print("Cliente excluído com sucesso!")
            else:
                print("Cliente não encontrado.")

        case "4":
            print("\n=== Lista de Clientes ===")

            if len(cadastro) == 0:
                print("Nenhum cliente cadastrado.")
            else:
                for cliente in sorted(cadastro):
                    dados = cadastro[cliente]

                    print("-" * 30)
                    print("Cliente:", cliente)
                    print("Idade:", dados["idade"])
                    print("Telefone:", dados["telefone"])

        case "5":
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida.")
