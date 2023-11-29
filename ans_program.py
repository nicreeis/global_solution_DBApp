reclamacoes = {}
total_geral_reclamacoes = 0

while True:
    print("Seja bem-vindo ao sistema de Avaliação de Operadoras da ANS")
    inicio = input("\nDeseja iniciar sua avaliação? S ou N: ").upper()

    if inicio in ["S", "SIM"]:
        for _ in range(5):
            operadora = input("Digite o nome da operadora: ")
            reclamacoes[operadora] = []

            while True:
                nome_cliente = input("Digite o nome do cliente ou 'sair' para encerrar as reclamações para esta operadora: ")

                if nome_cliente.lower() == 'sair':
                    break  

                motivo_reclamacao = input("Digite o motivo da reclamação: ")
                reclamacoes[operadora].append((nome_cliente, motivo_reclamacao))
                total_geral_reclamacoes += 1

                print(f"\nReclamações para a operadora {operadora}:")
                for cliente, motivo in reclamacoes[operadora]:
                    print(f"Cliente: {cliente}\nMotivo: {motivo}")

                total_operadora = len(reclamacoes[operadora])
                print(f"Total de reclamações para {operadora}: {total_operadora}\n")
                continuar = input("Deseja registrar outra reclamação para esta operadora? S ou N: ").upper()
                if continuar not in ["S", "SIM"]:
                    break

            continuar_outra_operadora = input("Deseja registrar uma reclamação para outra operadora? S ou N: ").upper()
            if continuar_outra_operadora not in ["S", "SIM"]:
                break  
                
        print(f"Total geral de reclamações feitas: {total_geral_reclamacoes}")
        print("Agradecemos pela participação!")
        break

    elif inicio in ["N", "NAO", "NÃO"]:
        print("Tenha um ótimo dia!")
        break
    else:
        print("Por favor, responda com 'S' para sim ou 'N' para não.")
