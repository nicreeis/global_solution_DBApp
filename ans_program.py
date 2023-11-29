#nicole
reclamacoes = {}
total_geral_reclamacoes = 0

while True:
    print("Seja bem-vindo ao sistema de Reclamação de Operadoras da ANS")
    inicio = input("\nDeseja iniciar sua avaliação? S ou N: ").upper()

    if inicio in ["S", "SIM"]:
        for _ in range(5):
            operadora = input("\nDigite o nome da operadora: ")
            reclamacoes[operadora] = []

            while True:
                nome_cliente = input("\nDigite o nome do cliente ou 'sair' para encerrar as reclamações para esta operadora: ")
                if nome_cliente.lower() == 'sair':
                    break  

                motivo_reclamacao = input("\nDigite o motivo da reclamação: ")
                reclamacoes[operadora].append((nome_cliente, motivo_reclamacao))
                total_geral_reclamacoes += 1

                print(f"\nReclamações para a operadora {operadora}:")
                for cliente, motivo in reclamacoes[operadora]:
                    print(f"\nCliente: {cliente}\nMotivo: {motivo}\n")

                total_operadora = len(reclamacoes[operadora])
                print(f"\nTotal de reclamações para {operadora}: {total_operadora}\n")
                continuar = input("\nDeseja registrar outra reclamação para esta operadora? S ou N: ").upper()
                if continuar in ["N", "NAO", "NÃO"]:
                    break

            continuar_outra_operadora = input("Deseja registrar uma reclamação para outra operadora? S ou N: ").upper()
            if continuar_outra_operadora in ["N", "NAO", "NÃO"]:
                break

        print(f"\nTotal geral de reclamações feitas: {total_geral_reclamacoes}")
        print("\nAgradecemos pela participação!")
        break

    elif inicio in ["N", "NAO", "NÃO"]:
        print("\nTenha um ótimo dia!")
        break
    else:
        print("\nPor favor, responda com 'S' para sim ou 'N' para não.")