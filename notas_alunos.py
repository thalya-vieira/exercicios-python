print("\n=== Controle de notas ===")
media = 0
cadastro = {}

while True :
    adicionar = input("\nCasdastrar aluno?[S/N] ")

    if(adicionar == "S" or adicionar == "s"):
        aluno = input("Aluno: ")
        nota1 = float(input("1ª nota: "))
        nota2 = float(input("2ª nota: "))
        media = (nota1+nota2)/2

        if(media>7 and media<=10):
            status = "Aprovado"
        elif(media>=0 and media<6.9):
            status = "Reprovado"
        else:
            status = "erro nas nota"
            
        cadastro[aluno] = {
            "nota1" : nota1,
            "nota2" : nota2,
            "media" : media,
            "status" : status
        }

    elif(adicionar == "N" or adicionar == "n"):
        print("Finalizado.")
        break

    else:
        print("Opcao inválida")
    

print("\n=== Media dos alunos ===")
for aluno in (cadastro):
    dados = cadastro[aluno]
    print("", aluno, "",dados["media"], "", dados["status"])