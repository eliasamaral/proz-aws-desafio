def calculadora():
    while True:
        print("Escolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        escolha = input("Digite o número da operação: ")
        
        if escolha == '0':
            print("Saindo...")
            break
        elif escolha in ['1', '2', '3', '4']:

            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
                continue
            

            if escolha == '1':
                resultado = num1 + num2
                print(f"O resultado da soma é: {resultado}")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"O resultado da subtração é: {resultado}")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"O resultado da multiplicação é: {resultado}")
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"O resultado da divisão é: {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Essa opção não existe.")
        
calculadora()
