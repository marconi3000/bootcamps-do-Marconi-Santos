asterisco = "+"*34
menu = f"""
{asterisco}
*   SELECIONE UMA OPÇÃO VÁLIDA   *
{asterisco}
*[1] Depositar\t\t\t *
* \t[2] Sacar\t\t *
* \t\t[3] Extrato\t *
* \t\t\t[0] Sair *
{asterisco}\n
=> """

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\n============== DEPÓSITO ================")
        valor = float(input("\tINFORME O VALOR DO DEPÓSITO: \n========================================\n\tR$ "))

        if valor > 0:
            saldo += valor
            extrato += f"VALOR DEPOSITADO: R$ {valor:.2f}\n"
            print("========================================")
            print("DEPÓSITO REALIZADO COM SUCESSO!")
            print("========================================")
            print(f"SALDO ATUAL: R$ {saldo:.2f}")
            print("========================================")
        else:
            print("========================================")
            print("FALHA NA OPERAÇÃO - TENTE NOVAMENTE")
            print("========================================")

    elif opcao == "2":
        print("\n============== SAQUE ================")
        valor = float(input("\tINFORME O VALOR DO SAQUE: \n=====================================\n\tR$ "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("==========================================")
            print("\tNÃO REALIZADO - POR MOTIVO DE SALDO INSUFICIENTE! \n========================================\n\tR$ ")

        elif excedeu_limite:
          print("==========================================")
          print("\tNÃO REALIZADO - O VALOR EXCEDEU O LIMITE!  \n========================================\n\tR$ ")

        elif excedeu_saques:
            print("==========================================")
            print("\tNÃO REALIZADO - QUANTIDADE DE SAQUE DIÁRIO INSUFICIENTE!  \n========================================\n\tR$ ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("==========================================")
            print("SAQUE REALIZADO COM SUCESSO!")
            print("==========================================")
            print(f"SALDO ATUAL: R$ {saldo:.2f}")
            print("==========================================")

        else:
            print("==========================================")
            print("\tNÃO REALIZADO - OPERAÇÃO INVÁLIDA")
            print("==========================================")

    elif opcao == "3":
        print("\n*************** EXTRATO ****************")
        print("\tNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\n\t\tSaldo: R$ {saldo:.2f}")
        print("******************************************")

    elif opcao == "0":
        print("==================================================")
        print("\t   ATÉ LOGO - OBRIGADO!")
        print("==================================================")
        break

    else:
        print("===========================================================")
        print("\t OPÇÃO INFORMADA NÃO EXISTE - TENTE NOVAMENTE")
        print("===========================================================")