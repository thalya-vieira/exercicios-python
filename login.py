
tentativa = 1
print("\nLOGIN- 5 tentativa")
while (tentativa <=5 ):
    usuario = input("Usuário: ")
    senha = int(input("Senha: "))
    tentativa = tentativa+1

    if(usuario == "thalya" and senha == 123):
        print("Acesso liberado")
        break
    else:
        print("Inválido. Tenta novamente\n")

    if(tentativa>5):
        print("Atingiu limite de tentativas")

    