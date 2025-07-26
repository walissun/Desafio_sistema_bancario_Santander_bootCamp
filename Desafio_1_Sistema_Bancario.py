menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 2500  # limite máximo por saque
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
limite_credito = 200  # limite de crédito disponível

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        valor_disponivel = saldo + limite_credito

        excedeu_disponivel = valor > valor_disponivel
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_disponivel:
            print("Operação falhou! Você ultrapassou seu saldo + limite de crédito.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite por operação.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor  # saldo pode ficar negativo se usar crédito
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        if saldo < 0:
            print(f"Crédito utilizado: R$ {-saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        print("Encerrando... Obrigado por usar o sistema bancário!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")