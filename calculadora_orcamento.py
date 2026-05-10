#     5. Calculadora de Orçamento
# Uma assistência técnica precisa gerar orçamentos rápidos.
# Desafio:
# Desenvolver um sistema que:
#         ◦ Receba peças e valores
#         ◦ Calcule mão de obra
#         ◦ Gere valor total do serviço

print("\n=== Calculo de orcamento ===")

lista_pecas = {}
mao_de_obra = 180.00

while True:
    adicionar = input("\nAdicionar pecas?[S/N] ")

    if(adicionar == "S" or adicionar == "s"):

        peca = input("Peça: ")
        valor_peca = float(input("Valor da peça: "))
        
        lista_pecas[peca] = {
            "valor_peca" : valor_peca
        }
        
        print("Peça adicionada")

    elif(adicionar == "N" or adicionar == "n"): 
        valor_peca = 0
        print("Finalizando orçamento")
        break
    
    else:
        print("Opcao inválida")


valor_total = mao_de_obra + valor_peca

print("\n=== Orçamento completo ===")
print("- Mão de obra ", mao_de_obra)

for peca in (lista_pecas):
    dados = lista_pecas[peca]

    print("-", peca, " ", dados["valor_peca"])

print("# Valor total:  ", valor_total)