print("=== Classificador de Cliente ===")

idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal do cliente: R$ ").replace(",", "."))

if renda < 2000:
    categoria = "Bronze"
elif renda < 5000:
    categoria = "Prata"
elif renda < 10000:
    categoria = "Ouro"
else:
    categoria = "Diamante"

print(f"Cliente com {idade} anos e renda de R$ {renda:.2f}.")
print(f"Categoria: {categoria}")