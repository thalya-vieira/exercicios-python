#     4. Controle de Frequência de Funcionários
# Uma empresa quer automatizar o controle de presença.
# Desafio:
# Criar um programa que:
#         ◦ Registre entrada e saída
#         ◦ Calcule horas trabalhadas
#         ◦ Informe atrasos automaticamente


from datetime import datetime
funcionarios = {}

print("\n=== Registro de frequencia ===")
print("Horário de Entrada 8:00 | Horário de saída 18:00")

while True:

    opcao = input("\nDeseja registrar presença?[s/n] ")

    if(opcao == "s" or opcao == "S"):

        # entrada de dados
        nome = input("Nome: ")
        hora_chegada = input("Horario chegada: ")
        hora_saida = input("Horario saida: ")

        # transformar o horario string em hora
        # formato = "%H:%M"
        chegada = datetime.strptime(hora_chegada, "%H:%M")
        saida = datetime.strptime(hora_saida, "%H:%M")

        # horario de serviço
        diferenca = saida - chegada

        print("Horas trabalhadas: ", diferenca)

        # mostra se o funcionario ta atrasado
        if(chegada.hour > 8 or (chegada.hour == 8 and chegada.minute > 0)):
            print("Atrasado")
        else:
            print("Pontual")


    elif (opcao == "n" or opcao == "N"):
        print("Finalizar")
        break

    else:
        print("Opcao inválida")