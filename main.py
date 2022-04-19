while 1:
    print("Que cálculo deseja realizar: ")
    print("1. Adição")
    print("2. Subtração")
    print("3  Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    choice = int(input("Digite o numero correspondente da função escolhida: "))
    if choice == 1:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        print("Output: ", num1+num2)
    elif choice == 2:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        print("Output: ", num1-num2)
    elif choice == 3:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        print("Output: ", num1*num2)
    elif choice == 4:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        print("Output: ", num1/num2)
    elif choice == 5:
        print("saindo...")
        break
    print()