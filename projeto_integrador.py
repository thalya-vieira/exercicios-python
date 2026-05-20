cadastro_livros = {}
cadastro_usuario = {}
lista_emprestimo = {}
id_emprestimo=0
while(True):

    print("\n=== bibioteca virtual ===")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuario")
    print("3. Emprestar livro")
    print("4. Devolução de livro")
    print("5. Consultar disponibilidade")
    print("6. Relatório de livros emprestados")
    print("7. Sair")
    opcao = input("Opcao: ")


    match opcao:

        case "1":

            livro = input("Nome livro: ")
            autor = input("Autor: ")
            quantidade = int(input("Quantidade: "))

            cadastro_livros[livro] = {
                "autor" : autor,
                "quantidade" : quantidade
            }

            print("--- livro adicionado! ---")
            
        case "2":
            usuario = input("Nome usuario: ")
            email = input("Email: ")
            ra = int(input("Identificacao RA: "))

            cadastro_usuario[usuario] = {
                "email" : email,
                "ra" : ra
            }
            print("--- usuario cadastrado! ---")
        
        case "3": 
            
            emp_livro = input("Livro: ")
            emp_usuario = input("Usuario: ")
            # -----------------------------------------------

            # se o usuario existe no cadastro de usuario
            if emp_usuario in cadastro_usuario:


                # indentifico se tem livro na lista de cadastro de livro
                if emp_livro in cadastro_livros:
                    
                    #se quantidade de livro no cadastro for maior q 0 ele pode ser emprestado
                    if cadastro_livros[emp_livro]["quantidade"] > 0:
                        id_emprestimo +=1

                        lista_emprestimo[id_emprestimo] = {
                            "livro" : emp_livro,
                            "usuario" : emp_usuario
                        }

                        cadastro_livros[emp_livro]["quantidade"] -= 1

                        print("--- Emprestimo realizado ---")
                    else:
                        print("--- Livro indisponivel ---")
                else:
                    print("--- livro nao encontrado ---")    
            else:
                print("--- Usuario nao encontrado! ---")


            # -------------------------------------------------
            

        case "4": 
            emp_livro = input("Livro: ")
            emp_usuario = input("Usuario: ")

            encontrado = False

            for id, dados in lista_emprestimo.items():

                if dados["livro"]== emp_livro and dados["usuario"]== emp_usuario:
                    cadastro_livros[emp_livro]["quantidade"] +=1
                    print("Livro devolvido")

                    del lista_emprestimo[id]

                    encontrado = True
                    break
            
            if not encontrado:
                print("--- Emprestimo nao encontrado ---")

        case "5":

            consulta = input("Consultar livro: ")
            
            #primeiro saber se consulta existe em cadastro
            if consulta in cadastro_livros:
                    
                emprestado =0 

                #colocar a lista de emprestimo para rodar
                for id, dados in lista_emprestimo.items():
                    
                    #se a consulta ser igual a livro, emprestimo soma
                    if consulta == dados["livro"]:
                        emprestado +=1

                print("-"*30)
                print(f"A consulta do livro {consulta}")
                print(f"emprestado: {emprestado}")
                print(f"estoque: {cadastro_livros[consulta]['quantidade']}")
                print("-"*30)

            else:
                print("--- O livro consultado nao esta no cadastro ---")      


        case "6":
            print("-"*30)
            print("Relatorio dos livros emprestados")

            for id, dados in lista_emprestimo.items():
                print(f"{id} - Livro: {dados['livro']} | Usuario: {dados['usuario']}")

            print("-"*30)


        case "7":
            print("Saindo...")
            break
        case _: 
            print("Tente novamente")


