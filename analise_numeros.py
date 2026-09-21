print("=== Análise de Números ===")

numeros = []

for posicao in range(1, 6):
    numero = float(input(f"Digite o {posicao}º número: ").replace(",", "."))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")