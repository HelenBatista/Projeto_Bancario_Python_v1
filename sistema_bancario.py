menu = """
Olá, bem vindo!!
Escolha uma opção:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Insira o número do deposito: "))

        if valor > 0: 
            print(f"Seu saldo é de R$ {valor:.2f}")
            saldo =+ valor
        else:
            print("Valor invalido para deposito!")

    elif opcao == "s":
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        saque = float(input("Digite o valor que deseja sacar: "))
        
        if excedeu_saques:
            print("Limite de saques diários atingido!")
        elif saque < saldo:
            if saque > 500:
                print("Saque inválido, o limite de saque é R$ 500.00")
            elif saque > 0:    
                saldo -= saque
                print("Saque feito com sucesso! O seu novo saldo é: R$", saldo)
                extrato += f"Saldo R$ {saldo:.2f}\n"
                numero_saques += 1
            else:
                print("Saque inválido, digite um valor positivo!")    
        
        else:
            print("Você não possui saldo suficiente, seu saldo atual é: R$", saldo)
        
    elif opcao == "e":
       print("-----------EXTRATO-------------")
       print(f"Você depositou R$ {valor:.2f}")
       if not extrato:
           print("Não foi realizado saques.")
       else:
           (extrato)
       print(f"Você tem R$ {saldo:.2f} de saldo em conta")
       print("-------------------------------")
        
    elif opcao == "q":
       print("Obrigado por usar nosso sistema")
       break
