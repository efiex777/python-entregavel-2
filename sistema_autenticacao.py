print("=== Sistema de Autenticação ===")

senha_correta = "python123"
tentativas = 0
acesso_liberado = False

while tentativas < 3 and not acesso_liberado:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        acesso_liberado = True
        print(f"Acesso liberado na tentativa {tentativas}.")
    else:
        tentativas_restantes = 3 - tentativas
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}.")

if not acesso_liberado:
    print("Acesso bloqueado após 3 tentativas incorretas.")