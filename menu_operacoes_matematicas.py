print("=== Menu de Operações Matemáticas ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha uma operação: ")
primeiro_numero = float(input("Digite o primeiro número: ").replace(",", "."))
segundo_numero = float(input("Digite o segundo número: ").replace(",", "."))

match opcao:
    case "1":
        resultado = primeiro_numero + segundo_numero
        nome_operacao = "soma"
    case "2":
        resultado = primeiro_numero - segundo_numero
        nome_operacao = "subtração"
    case "3":
        resultado = primeiro_numero * segundo_numero
        nome_operacao = "multiplicação"
    case "4":
        if segundo_numero == 0:
            print("Erro: não é possível dividir por zero.")
        else:
            resultado = primeiro_numero / segundo_numero
            nome_operacao = "divisão"
    case _:
        print("Opção inválida.")

if opcao in {"1", "2", "3"} or (opcao == "4" and segundo_numero != 0):
    print(f"Resultado da {nome_operacao}: {resultado}")