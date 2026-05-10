# Uma farmácia precisa organizar filas de atendimento.
# Desafio:
# Criar um sistema que:
#         ◦ Gere senhas automáticas
#         ◦ Mostre próxima senha
#         ◦ Controle fila preferencial


print("=== Gerador de senhas ===")
normal = 0
preferencia = 0

while True:
    print("1. Senha Normal")
    print("2. Senha Preferencial")
    print("3. Sair")
    opcao = input("Digite sua opcao: ")

    match opcao:
        case "1":
            normal += 1
            print(f"Senha Normal: N{normal:03}")
            print("\n")
        case "2":
            preferencia += 1
            print(f"Senha preferencial: P{preferencia:03}")
            print("\n")
        case "3":
            print("Sair")
            break
        case _:
            print("inválido")
            print("\n")

